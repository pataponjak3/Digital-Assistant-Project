from abc import ABC, abstractmethod

class LLMAdapter(ABC):

    @abstractmethod
    def chat(self, input: str, is_user_message: bool=True) -> str:
        """
        Send a chat message to the LLM and get a response.
        
        :param user_input: Message.
        :type user_input: str
        :param user_message: Boolean indicating if the input is from the user.
        :type user_message: bool
        :return: Answer of the LLM.
        :rtype: str
        """
        