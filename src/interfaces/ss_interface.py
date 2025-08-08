from abc import ABC, abstractmethod
from typing import Optional

class SpeechSynthesizer(ABC):
    @abstractmethod
    def synthesize_speech(self, text: str) -> Optional[str]:
        """Method that synthesizes speech"""

    @abstractmethod
    def stop_speech(self):
        """Method that stops the speech synthesis"""