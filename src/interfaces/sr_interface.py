from abc import ABC, abstractmethod
from typing import Optional

class SpeechRecognizer(ABC):
    @abstractmethod
    def recognize_speech(self, text: str) -> Optional[str]:
        """Method that recognizes speech"""
    
    @abstractmethod
    def list_microphones(self):
        """"Method that lists available working microphones"""

    @abstractmethod
    def select_microphone(self, index: int):
        """Method that selects a microphone by its index"""