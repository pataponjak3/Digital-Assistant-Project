from abc import ABC, abstractmethod

class LLMAdapter(ABC):
    @abstractmethod
    def chat(self, input: str, user_message: bool) -> str:
        """
        Send a chat message to the LLM and get a response.
        :param user_input: Message.
        :param user_message: Boolean indicating if the input is from the user.
        :return: Answer of the LLM.
        """
    
    @abstractmethod
    def handle_user_message(self, user_input: str) -> str:
        """
        Handle a user message by sending it to the LLM and processing the response. If the response contains a function call, execute it.
        :param user_input: Message from the user.
        :return: Processed response from the LLM.
        """