from abc import ABC, abstractmethod
from interfaces.backend_interface import Backend
from interfaces.sr_interface import SpeechRecognizer
from interfaces.ss_interface import SpeechSynthesizer
from typing import Optional

class ChatHandler(ABC):
    @property
    @abstractmethod
    def _backend(self) -> Backend:
        """
        Backend associated with the ChatHandler.

        :return: The Backend instance.
        :rtype: Backend
        """
    
    @property
    @abstractmethod
    def _sr(self) -> SpeechRecognizer:
        """
        Speech Recognizer associated with the ChatHandler.

        :return: The SpeechRecognizer instance.
        :rtype: SpeechRecognizer
        """
    
    @property
    @abstractmethod
    def _ss(self) -> SpeechSynthesizer:
        """
        Speech Synthesizer associated with the ChatHandler.

        :return: The SpeechSynthesizer instance.
        :rtype: SpeechSynthesizer
        """
    
    @abstractmethod
    def handle_chat_message(self, user_message: str):
        """
        Handle a chat message by sending it to the backend and processing the response.

        :param user_message: Message from the user.
        :type user_message: str
        :return: Processed response from the backend.
        :rtype: str
        """

    @abstractmethod
    def clear_chat_history(self):
        """
        Clear the chat history in the backend.
        """
    
    @abstractmethod
    def start_speech(self, text: str):
        """
        Speak the given text using the speech synthesizer.

        :param text: Text to be spoken.
        :type text: str
        """
    
    @abstractmethod
    def stop_speech(self):
        """
        Stop speaking using the speech synthesizer.
        """
    
    @abstractmethod
    def recognize_voice(self) -> Optional[str]:
        """
        Recognize speech from the microphone.

        :return: Recognized text or None if recognition fails.
        :rtype: Optional[str]
        """