import os
import re
import whisper
from flask import Flask, request, jsonify, send_file, render_template
from TTS.api import TTS

# FFmpeg path
os.environ["PATH"] += os.pathsep + r"C:\Users\wowin\Downloads\ffmpeg-8.1.1-essentials_build\ffmpeg-8.1.1-essentials_build\bin"

app = Flask(__name__)

print("Loading Coqui VITS...")
tts = TTS(model_name="tts_models/en/vctk/vits")

print("Loading Whisper...")
stt_model = whisper.load_model("large-v3")

OUTPUT_AUDIO = "outputs/api_output.wav"

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# TTS API
# -----------------------------
@app.route("/tts", methods=["POST"])
def text_to_speech():

    data = request.json

    text = data.get("text")

    speaker = data.get("speaker", "p225")

    if not text:
        return jsonify({
            "error": "Text is required"
        }), 400

    tts.tts_to_file(
        text=text,
        speaker=speaker,
        file_path=OUTPUT_AUDIO
    )

    return send_file(
        OUTPUT_AUDIO,
        mimetype="audio/wav",
        as_attachment=False
    )

# -----------------------------
# STT API
# -----------------------------
@app.route("/stt", methods=["POST"])
def speech_to_text():

    result = stt_model.transcribe(OUTPUT_AUDIO)

    return jsonify({
        "transcription": result["text"]
    })

# -----------------------------
# FULL PIPELINE API
# -----------------------------
@app.route("/pipeline", methods=["POST"])
def full_pipeline():

    data = request.json

    input_text = data.get("text")

    speaker = data.get("speaker", "p225")

    if not input_text:
        return jsonify({
            "error": "Text is required"
        }), 400

    # Generate speech
    tts.tts_to_file(
        text=input_text,
        speaker=speaker,
        file_path=OUTPUT_AUDIO
    )

    # Transcribe generated speech
    result = stt_model.transcribe(OUTPUT_AUDIO)

    transcribed_text = result["text"]

    # Accuracy checking
    clean_input = re.sub(r"[^\w\s]", "", input_text.lower()).strip()

    clean_output = re.sub(r"[^\w\s]", "", transcribed_text.lower()).strip()

    accuracy = "Perfect Match"

    if clean_input != clean_output:
        accuracy = "Minor Differences Detected"

    return jsonify({
        "input_text": input_text,
        "transcription": transcribed_text,
        "accuracy": accuracy
    })

# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)