from abc import ABC, abstractmethod
from ..interfaces.functionality_interface import Functionality

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
    def generate(self) -> str:
        """
        Generate the system prompt based on the functionalities available in the system.
        
        :return: The generated system prompt.
        :rtype: str
        """