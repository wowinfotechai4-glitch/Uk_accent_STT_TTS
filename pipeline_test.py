import os
import re
import whisper
from TTS.api import TTS

# FFmpeg path
os.environ["PATH"] += os.pathsep + r"C:\Users\wowin\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

print("Loading Coqui VITS...")

tts = TTS(model_name="tts_models/en/vctk/vits")

print("Loading Whisper...")

stt_model = whisper.load_model("large-v3")

input_text = input("\nEnter text:\n\n")

audio_path = "outputs/realtime.wav"

print("\nGenerating Speech...\n")

tts.tts_to_file(
    text=input_text,
    speaker="p225",
    file_path=audio_path
)

print("Speech Generated Successfully")

print("\nRunning Speech-to-Text...\n")

result = stt_model.transcribe(audio_path)

transcribed_text = result["text"]

print("Transcription Result:\n")

print(transcribed_text)

# Clean punctuation for better comparison
clean_input = re.sub(r"[^\w\s]", "", input_text.lower()).strip()
clean_output = re.sub(r"[^\w\s]", "", transcribed_text.lower()).strip()

print("\nAccuracy Check:\n")

if clean_input == clean_output:
    print("Perfect Match")
else:
    print("Minor Differences Detected")