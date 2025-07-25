# WAV HTTP

```bash
# Uplaod
curl -F "file=@input.wav" http://localhost:8080/upload/myfile.wav
# Download
curl http://localhost:8080/download/myfile.wav -o output.wav

# Change Sample Rate
curl -X POST http://localhost:8080/resample/myfile.wav \
  -H "Content-Type: application/json" \
  -d '{"new_sample_rate":16000}'

# Convert WAV to 8-bit:
curl -X POST http://localhost:8080/convert/myfile.wav \
  -H "Content-Type: application/json" \
  -d '{"bits_per_sample":8}'

# Change Volume (50%)
curl -X POST http://localhost:8080/volume/myfile.wav \
  -H "Content-Type: application/json" \
  -d '{"factor":0.5}'

# Convert a WAV to 8-bit µ-law
curl -X POST http://localhost:8080/convert/myfile.wav \
  -H "Content-Type: application/json" \
  -d '{"format":"mulaw8"}'
# Convert to 24-bit PCM
curl -X POST http://localhost:8080/convert/myfile.wav \
  -H "Content-Type: application/json" \
  -d '{"format":"pcm24"}'

```