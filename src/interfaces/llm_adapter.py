from abc import ABC, abstractmethod

class LLMAdapterInterface(ABC):
    @abstractmethod
    def chat(self, input: str, user_message: bool) -> str:
        """
        Send a chat message to the LLM and get a response.
        :param user_input: Message.
        :param user_message: Boolean indicating if the input is from the user.
        :return: Answer of the LLM.
        """