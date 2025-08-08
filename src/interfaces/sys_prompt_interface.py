from abc import ABC, abstractmethod

class SystemPromptGenerator(ABC):
    @abstractmethod
    def generate(self) -> str:
        """
        Generate the system prompt based on the functionalities available in the system.
        
        :return: The generated system prompt.
        :rtype: str
        """