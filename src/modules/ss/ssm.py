from .ss import SpeechSynthesizer
import pyttsx3

class SpeechSynthesisModule(SpeechSynthesizer):
    def __init__(self):
        self.engine = pyttsx3.init()
    
    def synthesize_speech(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()