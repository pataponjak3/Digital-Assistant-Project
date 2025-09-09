from abc import ABC, abstractmethod
from ..types.types import LLMResponse

class LLMAdapter(ABC):

    @abstractmethod
    def chat(self, input: str, is_not_da_response: bool=True, supports_function_calls: bool=False) -> LLMResponse:
        """
        Send a chat message to the LLM and get a response.
        
        :param user_input: Message.
        :type user_input: str
        :param is_not_da_response: Boolean indicating if the input is not an answer from the LLM, default is True.
        :type user_message: bool
        :return: Answer of the LLM, which can be a response or a function call.
        :rtype: LLMResponse
        """
        