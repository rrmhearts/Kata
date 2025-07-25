use axum::{
    extract::{Path, Multipart},
    http::StatusCode,
    response::{IntoResponse, Response},
    routing::{get, post},
    Json, Router,
};
use bytes::Bytes;
use hound::{WavReader, WavSpec, WavWriter};
use std::{
    collections::HashMap,
    io::{Cursor, Read, Seek, Write},
    net::SocketAddr,
    sync::{Arc, Mutex},
};

type Storage = Arc<Mutex<HashMap<String, Vec<u8>>>>;

fn linear_to_mulaw(sample: i16) -> u8 {
    const MU: i16 = 255;
    let sign = if sample < 0 { 0x80 } else { 0x00 };
    let magnitude = (sample.abs() as i32).min(0x7FFF) >> 2;

    let exponent = ((magnitude >> 7) & 0x0F) as u8;
    let mantissa = ((magnitude >> (exponent + 3)) & 0x0F) as u8;

    !(sign | (exponent << 4) | mantissa)
}

fn write_mulaw_wav(samples: &[i16], sample_rate: u32, channels: u16) -> Vec<u8> {
    let mut data: Vec<u8> = Vec::new();

    // Encode samples
    let encoded: Vec<u8> = samples.iter().map(|s| linear_to_mulaw(*s)).collect();

    let num_samples = encoded.len() as u32;
    let block_align = channels;
    let byte_rate = sample_rate * block_align as u32;

    // Write RIFF header
    let mut buffer = Cursor::new(Vec::new());

    let data_chunk_size = num_samples;
    let fmt_chunk_size = 18u32;
    let total_size = 4 + (8 + fmt_chunk_size) + (8 + data_chunk_size);

    buffer.write_all(b"RIFF").unwrap();
    buffer.write_all(&(total_size as u32).to_le_bytes()).unwrap();
    buffer.write_all(b"WAVE").unwrap();

    // fmt chunk
    buffer.write_all(b"fmt ").unwrap();
    buffer.write_all(&fmt_chunk_size.to_le_bytes()).unwrap(); // chunk size
    buffer.write_all(&7u16.to_le_bytes()).unwrap(); // format code 7 = µ-law
    buffer.write_all(&channels.to_le_bytes()).unwrap();
    buffer.write_all(&sample_rate.to_le_bytes()).unwrap();
    buffer.write_all(&byte_rate.to_le_bytes()).unwrap();
    buffer.write_all(&block_align.to_le_bytes()).unwrap();
    buffer.write_all(&8u16.to_le_bytes()).unwrap(); // bits per sample
    buffer.write_all(&0u16.to_le_bytes()).unwrap(); // extra bytes

    // data chunk
    buffer.write_all(b"data").unwrap();
    buffer.write_all(&(data_chunk_size as u32).to_le_bytes()).unwrap();
    buffer.write_all(&encoded).unwrap();

    buffer.into_inner()
}

#[tokio::main]
async fn main() {
    let storage: Storage = Arc::new(Mutex::new(HashMap::new()));

    let app = Router::new()
        .route("/upload/:name", post(upload))
        .route("/download/:name", get(download))
        .route("/resample/:name", post(resample))
        .route("/convert/:name", post(convert_format))   // NEW
        .route("/volume/:name", post(adjust_volume))     // NEW
        .with_state(storage.clone());


    let addr = SocketAddr::from(([127, 0, 0, 1], 8080));
    println!("Server listening on http://{}", addr);
    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();
}

async fn upload(
    Path(name): Path<String>,
    state: axum::extract::State<Storage>,
    mut multipart: Multipart,
) -> Response {
    while let Some(field) = multipart.next_field().await.unwrap() {
        let data = field.bytes().await.unwrap().to_vec();
        state.lock().unwrap().insert(name.clone(), data);
        return Response::builder().status(200).body("Uploaded".into()).unwrap();
    }
    (StatusCode::BAD_REQUEST, "No file received").into_response()
}

async fn download(Path(name): Path<String>, state: axum::extract::State<Storage>) -> Response {
    let files = state.lock().unwrap();
    if let Some(data) = files.get(&name) {
        Response::builder()
            .header("Content-Type", "audio/wav")
            .header("Content-Disposition", format!("attachment; filename=\"{}\"", name))
            .body(axum::body::Body::from(data.clone()))
            .unwrap()
    } else {
        (StatusCode::NOT_FOUND, "File not found").into_response()
    }
}

#[derive(serde::Deserialize)]
struct ResampleParams {
    new_sample_rate: u32,
}

async fn resample(
    Path(name): Path<String>,
    state: axum::extract::State<Storage>,
    Json(params): Json<ResampleParams>,
) -> Response {
    let mut files = state.lock().unwrap();

    let original = match files.get(&name) {
        Some(f) => f.clone(),
        None => return (StatusCode::NOT_FOUND, "File not found").into_response(),
    };

    // Read original WAV file
    let mut reader = WavReader::new(Cursor::new(&original)).unwrap();
    let spec = reader.spec();
    let samples: Vec<i16> = reader.samples::<i16>().map(|s| s.unwrap()).collect();

    // Naive resample: just skip samples
    let factor = spec.sample_rate as f32 / params.new_sample_rate as f32;
    let resampled: Vec<i16> = samples
        .iter()
        .enumerate()
        .filter(|(i, _)| (*i as f32 % factor).round() == 0.0)
        .map(|(_, &s)| s)
        .collect();

    let new_spec = WavSpec {
        channels: spec.channels,
        sample_rate: params.new_sample_rate,
        bits_per_sample: 16,
        sample_format: hound::SampleFormat::Int,
    };

    let mut buffer = Cursor::new(Vec::new());
    {
        let mut writer = WavWriter::new(&mut buffer, new_spec).unwrap();
        for s in resampled {
            writer.write_sample(s).unwrap();
        }
        writer.finalize().unwrap();
    }

    // Store modified
    files.insert(name.clone(), buffer.into_inner());

    Response::builder()
        .status(200)
        .body("Resampled successfully".into())
        .unwrap()
}

#[derive(serde::Deserialize)]
#[serde(rename_all = "lowercase")]
enum TargetFormat {
    Pcm8,
    Pcm16,
    Pcm24,
    Mulaw8,
}

#[derive(serde::Deserialize)]
struct FormatConversionParams {
    format: TargetFormat,
}

async fn convert_format(
    Path(name): Path<String>,
    state: axum::extract::State<Storage>,
    Json(params): Json<FormatConversionParams>,
) -> Response {
    let mut files = state.lock().unwrap();

    let original = match files.get(&name) {
        Some(f) => f.clone(),
        None => return (StatusCode::NOT_FOUND, "File not found").into_response(),
    };

    let mut reader = match WavReader::new(Cursor::new(&original)) {
        Ok(r) => r,
        Err(_) => return (StatusCode::BAD_REQUEST, "Invalid WAV file").into_response(),
    };

    let spec = reader.spec();
    let samples: Vec<i16> = reader.samples::<i16>().filter_map(Result::ok).collect();

    let (bits, mut write_sample): (u16, Box<dyn FnMut(&mut WavWriter<&mut Cursor<Vec<u8>>>, i16) -> Result<(), hound::Error>>) = match params.format {
        TargetFormat::Pcm8 => (
            8,
            Box::new(|w, s| {
                let sample = (((s as i32 + 32768) >> 8) & 0xFF) as u8;
                w.write_sample(sample)
            }),
        ),
        TargetFormat::Pcm16 => (
            16,
            Box::new(|w, s| w.write_sample(s)),
        ),
        TargetFormat::Pcm24 => (
            24,
            Box::new(|w, s| {
                let s_24 = (s as i32) << 8;
                w.write_sample(s_24)
            }),
        ),
        TargetFormat::Mulaw8 => {
            let raw = write_mulaw_wav(&samples, spec.sample_rate, spec.channels);
            files.insert(name.clone(), raw);
            return Response::builder()
                .status(200)
                .body("Converted to µ-law".into())
                .unwrap();
        }

        // TargetFormat::Mulaw8 => (
        //     8,
        //     Box::new(|w, s| w.write_sample(linear_to_mulaw(s))),
        // ),
    };

    let new_spec = WavSpec {
        channels: spec.channels,
        sample_rate: spec.sample_rate,
        bits_per_sample: bits,
        sample_format: hound::SampleFormat::Int,
    };

    let mut buffer = Cursor::new(Vec::new());
    {
        let mut writer = WavWriter::new(&mut buffer, new_spec).unwrap();
        for s in &samples {
            write_sample(&mut writer, *s).unwrap();
        }
        writer.finalize().unwrap();
    }

    files.insert(name.clone(), buffer.into_inner());

    Response::builder()
        .status(200)
        .body("Format converted".into())
        .unwrap()
}

#[derive(serde::Deserialize)]
struct VolumeParams {
    factor: f32, // e.g. 0.5 = half volume, 2.0 = double
}

async fn adjust_volume(
    Path(name): Path<String>,
    state: axum::extract::State<Storage>,
    Json(params): Json<VolumeParams>,
) -> Response {
    let mut files = state.lock().unwrap();

    let original = match files.get(&name) {
        Some(f) => f.clone(),
        None => return (StatusCode::NOT_FOUND, "File not found").into_response(),
    };

    let reader = WavReader::new(Cursor::new(&original));
    if reader.is_err() {
        return (StatusCode::BAD_REQUEST, "Invalid WAV file").into_response();
    }

    let mut reader = reader.unwrap();
    let spec = reader.spec();

    let samples: Vec<i16> = reader.samples::<i16>().map(|s| s.unwrap()).collect();

    let adjusted_samples: Vec<i16> = samples
        .iter()
        .map(|s| {
            let scaled = (*s as f32) * params.factor;
            scaled.clamp(i16::MIN as f32, i16::MAX as f32) as i16
        })
        .collect();

    let mut buffer = Cursor::new(Vec::new());

    {
        let mut writer = WavWriter::new(&mut buffer, spec).unwrap();
        for s in adjusted_samples {
            writer.write_sample(s).unwrap();
        }
        writer.finalize().unwrap();
    }

    files.insert(name.clone(), buffer.into_inner());

    Response::builder()
        .status(200)
        .body("Volume adjusted".into())
        .unwrap()
}

