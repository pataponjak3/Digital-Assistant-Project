from interfaces.backend_interface import Backend
from interfaces.sr_interface import SpeechRecognizer
from interfaces.ss_interface import SpeechSynthesizer
from interfaces.chat_handler_interface import ChatHandler

class AssistantChatHandler(ChatHandler):
    def __init__(self, backend: Backend, ss: SpeechSynthesizer, sr: SpeechRecognizer):
        self.__backend = backend
        self.__sr = sr
        self.__ss = ss

    def _backend(self) -> Backend:
        return self.__backend
    
    def _sr(self) -> SpeechRecognizer:
        return self.__sr
    
    def _ss(self) -> SpeechSynthesizer:
        return self.__ss
    
    def handle_chat_message(self, user_message: str):
        response = self.__backend.handle_user_message(user_message)
        return response
    
    def clear_chat_history(self):
        self.__backend.clear_chat_history()
    
    def start_speech(self, text: str):
        self.__ss.synthesize_speech(text)

    def stop_speech(self):
        self.__ss.stop_speech()
    
    def recognize_voice(self):
        return self.__sr.recognize_speech()