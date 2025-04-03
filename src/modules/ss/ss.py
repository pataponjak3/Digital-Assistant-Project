from abc import ABC, abstractmethod

class SpeechSynthesizer(ABC):
    @abstractmethod
    def synthesize_speech(self):
        """Method that synthesizes speech"""