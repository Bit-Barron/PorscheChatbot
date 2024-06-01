from flask import Flask, request, jsonify
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
from flask_cors import CORS
import os
import tempfile

app = Flask(__name__)
CORS(app, origins="*")
class FastWhisperTranscriber:
    def __init__(self, model_size="large-v3", sample_rate=44100):
        self.model_size = model_size
        self.sample_rate = sample_rate
        self.model = WhisperModel(model_size, device="cpu", compute_type="float32")
        self.is_recording = False 

    def record_audio(self, duration=5):  # Ändere die Aufnahmedauer nach Bedarf
        frames_per_buffer = int(self.sample_rate * 0.5) 
        recording = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=2, dtype="float64")
        sd.wait()
        return recording

    def save_temp_audio(self, recording):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        write(temp_file.name, self.sample_rate, recording)
        return temp_file.name
    
    def transcribe_audio(self, file_path):
        segments, info = self.model.transcribe(file_path, beam_size=5)
        full_transcript = ""
        for segment in segments:
            full_transcript += segment.text + " "
        os.remove(file_path)
        return full_transcript
    
    def process_audio(self, audio_data):
        temp_file = self.save_temp_audio(audio_data)
        transcript = self.transcribe_audio(temp_file)
        return transcript

transcriber = FastWhisperTranscriber()

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'})
    audio_file = request.files['audio']
    audio_data = np.frombuffer(audio_file.read(), dtype=np.float64)
    transcript = transcriber.process_audio(audio_data)
    return jsonify({'transcript': transcript})

if __name__ == "__main__":
    app.run(debug=True)
