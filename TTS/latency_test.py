import time
from TTS.api import TTS

print("Loading Coqui VITS Model...")

start_model = time.time()

tts = TTS(model_name="tts_models/en/vctk/vits")

end_model = time.time()

model_loading_time = end_model - start_model

print(f"Model Loading Time: {model_loading_time:.2f} seconds")

text = "This is a latency performance testing sentence."

speaker = "p225"

print("Generating Speech...")

start_generation = time.time()

tts.tts_to_file(
    text=text,
    speaker=speaker,
    file_path="outputs/latency_test.wav"
)

end_generation = time.time()

generation_time = end_generation - start_generation

print(f"Speech Generation Time: {generation_time:.2f} seconds")

total_time = model_loading_time + generation_time

print(f"Total Processing Time: {total_time:.2f} seconds")