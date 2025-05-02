from abc import ABC, abstractmethod
from typing import Optional

class SpeechRecognizer(ABC):
    @abstractmethod
    def recognize_speech(self, text: str) -> Optional[str]:
        """Method that recognizes speech"""