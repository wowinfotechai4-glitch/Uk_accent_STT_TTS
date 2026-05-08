from TTS.api import TTS

print("Loading Coqui VITS...")

tts = TTS(model_name="tts_models/en/vctk/vits")

voice_profiles = {
    "assistant_female": "p225",
    "assistant_male": "p226",
    "narrator": "p227",
    "customer_support": "p228"
}

text = "Welcome to the adaptive voice testing system."

for role, speaker in voice_profiles.items():

    output_file = f"outputs/{role}.wav"

    print(f"Generating voice for: {role}")

    tts.tts_to_file(
        text=text,
        speaker=speaker,
        file_path=output_file
    )

print("Adaptive voice testing completed.")