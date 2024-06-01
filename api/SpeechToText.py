import sounddevice as sd
import numpy as np
import time
from pynput import keyboard
import tempfile
import os
from textToSpeech import get_solutions
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

print("##########################################################################")
print("# Welcome to the Speech to Text program. Press space to start recording. #")
print("##########################################################################")

class FastWhisperTranscriber:
    def __init__(self, model_size="large-v3", sample_rate=44100):
        self.model_size = model_size
        self.sample_rate = sample_rate
        self.model = WhisperModel(model_size, device="cpu", compute_type="float32")
        self.is_recording = False 

    def on_press(self, key):
        if key == keyboard.Key.space:
            if not self.is_recording:
                self.is_recording = True
                self.start_time = time.time()
                print("Recording... ")

    def on_release(self, key):
        if key == keyboard.Key.space:
            if self.is_recording:
                self.is_recording = False
                print("Recording stopped")
                return False

    def record_audio(self):
        recording = np.array([], dtype="float64").reshape(0, 2)
        frames_per_buffer = int(self.sample_rate * 0.5) 
        
        def on_press(key):
            self.on_press(key)

        def on_release(key):
            return self.on_release(key)
        
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            while True:
                if self.is_recording:
                    chunk = sd.rec(frames_per_buffer, samplerate=self.sample_rate, channels=2, dtype="float64")
                    sd.wait()
                    recording = np.vstack([recording, chunk])
                if not self.is_recording and len(recording) > 0:
                    break
            listener.join()
        
        print(f"Recorded audio shape: {recording.shape}")
        return recording

    def save_temp_audio(self, recording):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        write(temp_file.name, self.sample_rate, recording)
        print(f"Audio saved to temporary file: {temp_file.name}")
        return temp_file.name
    
    def transcribe_audio(self, file_path):
        segments, info = self.model.transcribe(file_path, beam_size=5)
        print(f"Detected language {info.language} with probability {info.language_probability:.2f}")
        full_transcript = ""
        for segment in segments:
            full_transcript += segment.text + " "
        os.remove(file_path)
        return full_transcript
    
    def run(self):
        while True:
            recording = self.record_audio()
            if recording is not None and len(recording) > 0:
                temp_file = self.save_temp_audio(recording)
                transcript = self.transcribe_audio(temp_file)
                print(transcript)
                get_solutions(transcript)
                end_time = time.time()
                print("Zeit für Frage und Antwort", end_time)
            print("Press space to start recording")

if __name__ == "__main__":
    transcriber = FastWhisperTranscriber()
    transcriber.run()
