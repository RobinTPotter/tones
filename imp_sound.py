import soundfile as sf
import sounddevice as sd

class sound():
    def __init__(self, wav):
        self.samples, self.samplerate = sf.read(wav)
        print(f"loaded {wav}")
    def play(self):
        sd.play(self.samples, self.samplerate)
        #sd.wait()


