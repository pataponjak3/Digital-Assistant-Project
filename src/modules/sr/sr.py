from abc import ABC, abstractmethod

class SpeechRecognizer(ABC):
    @abstractmethod
    def recognize_speech(self, text: str):
        """Method that recognizes speech"""