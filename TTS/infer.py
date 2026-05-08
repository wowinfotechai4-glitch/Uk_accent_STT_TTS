from TTS.api import TTS

print("Loading Coqui VITS...")

tts = TTS(model_name="tts_models/en/vctk/vits")

speakers = ["p225", "p226", "p227", "p228"]

text = "Good morning. Today we are testing emotional speech generation."

for speaker in speakers:

    output_path = f"outputs/{speaker}.wav"

    print(f"Generating voice for {speaker}")

    tts.tts_to_file(
        text=text,
        speaker=speaker,
        file_path=output_path
    )

print("All speech files generated successfully")