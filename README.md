# Real-Time Speech Recognition with Vosk

This project implements real-time speech recognition using the Vosk API and PyAudio. It transcribes microphone input in real-time and features automatic silence detection for hands-free operation.

## Features

- **Real-time speech-to-text** transcription
- **Silence-based auto-stop** functionality
- **Amplitude monitoring** for silence detection
- **Debug information** showing amplitude levels
- **Graceful termination** with proper resource cleanup

## Requirements

- Python 3.6+
- PyAudio
- Vosk
- NumPy

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/speech-recognition.git
   cd speech-recognition
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install vosk pyaudio numpy
   ```

4. Download the Vosk model:
   ```bash
   mkdir models
   # Download the vosk-model-small-en-us-0.15 model from https://alphacephei.com/vosk/models
   # Extract it to the models/ directory
   ```

## Usage

Run the script with:

```bash
python speech_recognition.py
```

The program will:
1. Load the Vosk model
2. Initialize your microphone
3. Begin listening and transcribing speech
4. Print recognized text to the console
5. Automatically stop after 5 seconds of silence

To manually stop the program, press `Ctrl+C`.

## Configuration

You can modify these parameters in the script:

- `SILENCE_THRESHOLD`: Amplitude threshold for silence detection (default: 200)
- `SILENCE_DURATION`: How long silence must persist before stopping (default: 5 seconds)
- `MODEL_PATH`: Path to the Vosk model directory

## How It Works

1. **Model Loading**: The script initializes the Vosk speech recognition model
2. **Audio Stream**: PyAudio opens a microphone stream with appropriate parameters
3. **Recognition Loop**: 
   - Audio is continuously captured from the microphone
   - NumPy calculates average amplitude for silence detection
   - Audio chunks are fed to the Vosk recognizer
   - Recognized text is printed to the console
4. **Silence Detection**: If audio amplitude stays below threshold for the specified duration, the program stops
5. **Cleanup**: Resources are properly released on exit

## Troubleshooting

- **No audio input detected**: Ensure your microphone is properly connected and configured as the default input device
- **Recognition accuracy issues**: Consider downloading a larger Vosk model for better accuracy
- **PyAudio installation errors**: On Linux, you may need to install portaudio development headers first (`sudo apt-get install portaudio19-dev`)

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.