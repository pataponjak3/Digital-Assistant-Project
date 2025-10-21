from interfaces.sr_interface import SpeechRecognizer
import speech_recognition as sr

class SpeechRecognitionModule(SpeechRecognizer):

    __recognizer = sr.Recognizer()
    __recognizer.dynamic_energy_threshold = True  # Enable dynamic energy thresholding
    __microphone = sr.Microphone()

    def recognize_speech(self):
        with self.__microphone as source:
            print("Listening...")
            self.__recognizer.adjust_for_ambient_noise(source)
            audio = self.__recognizer.listen(source)
        
        try:
            text = self.__recognizer.recognize_google(audio)
            print("Recognized:", text)
            return text, "ok"
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None, "unrecognized"
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None, "request_error"
    
    def list_microphones(self):
        return sr.Microphone.list_working_microphones()
    
    def select_microphone(self, index):
        try:
            self.__microphone = sr.Microphone(index)
        except IndexError:
            print("Invalid microphone index selected.")

