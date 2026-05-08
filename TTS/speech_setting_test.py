from TTS.api import TTS

print("Loading Coqui VITS...")

tts = TTS(model_name="tts_models/en/vctk/vits")

tests = {
    "normal":
    "Welcome to the UK accent speech research project.",

    "slow":
    "Welcome... to the UK accent speech research project.",

    "question":
    "Welcome to the UK accent speech research project?",

    "excited":
    "Welcome to the UK accent speech research project!",

    "long_pause":
    "Good morning.     Today we are testing speech pacing."
}

speaker = "p225"

for setting, text in tests.items():

    output_path = f"outputs/{setting}.wav"

    print(f"Generating: {setting}")

    tts.tts_to_file(
        text=text,
        speaker=speaker,
        file_path=output_path
    )

print("Speech setting tests completed.")