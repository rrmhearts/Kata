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

```