from abc import ABC, abstractmethod
from typing import Optional, Tuple

class SpeechRecognizer(ABC):
    @abstractmethod
    def recognize_speech(self) -> Tuple[Optional[str], str]:
        """
        Method that recognizes speech
        
        :return: A tuple (recognized_text, status), where recognized_text is the transcribed text or None if unrecognized, and status is a string indicating the result status ("ok", "unrecognized", "request_error")
        :rtype: Tuple[Optional[str], str]
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