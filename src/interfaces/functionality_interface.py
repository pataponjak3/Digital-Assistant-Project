from abc import ABC, abstractmethod
from typing import Callable

class Functionality(ABC):
    """Interface for functionalities of the DA"""

    @abstractmethod
    def get_functions_description(self) -> list[str]:
        """
        Definition of the functions' description.
        This is an important part of each functionality, because this will demonstrate to the DA how the function works.

        :return: A list of strings, each containing the description of a function.
        :rtype: list[str]
        """
    
    @abstractmethod
    def execute_function(self, name:str, args:dict) -> Callable[[dict], str]:
        """
        Execute the function with the given name and arguments.
        
        :param name: The name of the function to execute.
        :type name: str
        :param args: The arguments to pass to the function.
        :type args: dict
        :return: The result of the function's execution, which should be a string containing the response for the user.
        :rtype: str
        """