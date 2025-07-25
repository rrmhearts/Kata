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

#[tokio::main]
async fn main() {
    let storage: Storage = Arc::new(Mutex::new(HashMap::new()));

    let app = Router::new()
        .route("/upload/:name", post(upload))
        .route("/download/:name", get(download))
        .route("/resample/:name", post(resample))
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
            .body(Bytes::from(data.clone()))
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
