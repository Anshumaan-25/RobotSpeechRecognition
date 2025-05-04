from vosk import Model, KaldiRecognizer
import pyaudio
import json
import time
import numpy as np

# Initialize the Vosk model and recognizer
model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

# Set up the microphone input
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8192)
stream.start_stream()

# Silence detection parameters
silence_threshold = 150  # alter this according to your environment
silent_duration = 3  # Time in seconds before stopping automatically after silence
last_time = time.time()

print("Listening... Press Ctrl+C to stop.")

try:
    while True:
        data = stream.read(4096)
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Calculate the average amplitude of the audio
        avg_amplitude = np.mean(np.abs(audio_data))
        print(f"Average amplitude: {avg_amplitude}")  # Debugging line to track the amplitude
        
        # Check if the audio level is below the silence threshold
        if avg_amplitude < silence_threshold:
            if time.time() - last_time > silent_duration:
                print(f"No speech detected for {silent_duration} seconds. Stopping.")
                break
        else:
            last_time = time.time()  # Reset the silence timer when there's sound

        # Process the audio with Vosk recognizer
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            print("You said:", result.get("text", ""))
except KeyboardInterrupt:
    print("\nStopped listening.")
finally:
    # Cleanly stop the audio stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Audio stream closed and program terminated.")
