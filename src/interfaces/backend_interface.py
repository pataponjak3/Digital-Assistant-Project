from abc import ABC, abstractmethod
from ..interfaces.llm_adapter_interface import LLMAdapter
from ..interfaces.func_handler_interface import FunctionHandler

class Backend(ABC):

    @property
    @abstractmethod
    def _llm_adapter(self) -> LLMAdapter:
        """
        LLM Adapter associated with the Backend.

        :return: The LLM Adapter.
        :rtype: LLMAdapter
        """
        pass

    @property
    @abstractmethod
    def _function_handler(self) -> FunctionHandler:
        """
        Function Handler associated with the Backend.

        :return: The Function Handler.
        :rtype: FunctionHandler
        """
        pass
    
    @abstractmethod
    def handle_user_message(self, user_input: str) -> str:
        """
        Handle a user message by sending it to the LLM and processing the response. If the response contains a function call, execute it.
        
        :param user_input: Message from the user.
        :type user_input: str
        :return: Processed response from the LLM.
        :rtype: str
        """