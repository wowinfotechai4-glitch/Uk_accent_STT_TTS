from TTS.api import TTS

print("Loading Coqui VITS Model...")

tts = TTS(model_name="tts_models/en/vctk/vits")

emotions = {
    "happy": "I am extremely excited to welcome everyone today!",
    
    "sad": "I feel disappointed and very emotional today.",

    "angry": "This situation is absolutely unacceptable and frustrating.",

    "calm": "Today is a peaceful and relaxing day for everyone."
}

speaker = "p225"

for emotion, text in emotions.items():

    output_file = f"outputs/{emotion}.wav"

    print(f"Generating {emotion} speech...")

    tts.tts_to_file(
        text=text,
        speaker=speaker,
        file_path=output_file
    )

print("Emotional speech generation completed.")