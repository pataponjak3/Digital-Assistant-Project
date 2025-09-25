from interfaces.ss_interface import SpeechSynthesizer
import pyttsx3
import threading

class SpeechSynthesisModule(SpeechSynthesizer):
    __engine = pyttsx3.init()
    __lock = threading.Lock()

    def synthesize_speech(self, text):
        with self.__lock:
            self.__engine.say(text)
            self.__engine.runAndWait()
    
    def stop_speech(self):
        with self.__lock:
            self.__engine.stop()