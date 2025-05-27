from ...interfaces.sr import SpeechRecognizer
import speech_recognition as sr

class SpeechRecognitionModule(SpeechRecognizer):
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True  # Enable dynamic energy thresholding
        self.microphone = sr.Microphone()
        self.selected_microphone_index = None
    
    def recognize_speech(self):
        with self.microphone as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        
        try:
            text = self.recognizer.recognize_google(audio)
            print("Recognized:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None
    
    def list_microphones(self):
        return sr.Microphone.list_working_microphones()
    
    def select_microphone(self, index):
        try:
            self.microphone = sr.Microphone(device_index=index)
            self.selected_microphone = index
        except IndexError:
            print("Invalid microphone index selected.")

