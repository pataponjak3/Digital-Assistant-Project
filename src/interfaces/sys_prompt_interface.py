from abc import ABC, abstractmethod
from interfaces.functionality_interface import Functionality

class SystemPromptGenerator(ABC):

    @property
    @abstractmethod
    def _modules(self) -> dict[str, Functionality]:
        """
        Get the modules available in the system.

        :return: A dictionary of modules.
        :rtype: dict[str, Functionality]
        """
        pass


    @abstractmethod
    def generate(self, supports_function_calls: bool) -> str:
        """
        Generate the system prompt based on the functionalities available in the system.
        If the LLM supports function calls, don't include function descriptions in the prompt.


        :param supports_function_calls: Boolean indicating if the LLM supports function calls with specific role.
        :type supports_function_calls: bool
        :return: The generated system prompt.
        :rtype: str
        """