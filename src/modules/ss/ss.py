from abc import ABC, abstractmethod
from typing import Optional

class SpeechSynthesizer(ABC):
    @abstractmethod
    def synthesize_speech(self) -> Optional[str]:
        """Method that synthesizes speech"""