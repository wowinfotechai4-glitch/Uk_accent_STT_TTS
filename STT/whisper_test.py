import os

# Add FFmpeg path manually
os.environ["PATH"] += os.pathsep + r"C:\Users\wowin\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

import whisper

print("Loading Whisper Model...")

model = whisper.load_model("medium")

audio_file = "outputs/p225.wav"

print("Transcribing UK Accent Speech...")

result = model.transcribe(audio_file)

print("\nTranscription Result:\n")

print(result["text"])