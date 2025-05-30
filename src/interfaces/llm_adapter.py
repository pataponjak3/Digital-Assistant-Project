from abc import ABC, abstractmethod

class LLMAdapterInterface(ABC):
    @abstractmethod
    def chat(self, user_input: str) -> str:
        """
        Send a chat message to the LLM and get a response.
        :param user_input: Message of the user.
        :return: Answer of the LLM.
        """