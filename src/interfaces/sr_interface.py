from abc import ABC, abstractmethod
from typing import Optional

class SpeechRecognizer(ABC):
    @abstractmethod
    def recognize_speech(self) -> Optional[str]:
        """
        Method that recognizes speech
        
        :return: Recognized text or None if recognition fails
        :rtype: Optional[str]
        """
    
    @abstractmethod
    def list_microphones(self) -> dict[int, str]:
        """"
        Method that lists available working microphones
        
        :return: Dictionary of microphone indices and their names
        :rtype: dict[int, str]
        """

    @abstractmethod
    def select_microphone(self, index: int):
        """
        Method that selects a microphone by its index
        
        :param index: The index of the microphone to select
        :type index: int
        """