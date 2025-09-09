from abc import ABC, abstractmethod
from typing import Callable

class Functionality(ABC):
    """Interface for functionalities of the DA"""

    @abstractmethod
    def get_functions_description(self) -> list[str]:
        """
        Definition of the functions' description.
        This is an important part of each functionality, because this will demonstrate to the DA how the function works.
        Important for LLMs that do not support function calls natively.

        :return: A list of strings, each containing the description of a function.
        :rtype: list[str]
        """

    def get_functions_schema(self) -> list[dict]:
        """
        Definition of the functions' schema.
        This is an important part of each functionality, because this will demonstrate to the DA how the function works.
        Important for LLMs that support function calls natively.

        :return: A list of dictionaries, each containing the schema of a function.
        :rtype: list[dict]
        """
    
    @abstractmethod
    def execute_function(self, name:str, args:dict, supports_function_calls: bool) -> Callable[[dict], str | dict]:
        """
        Execute the function with the given name and arguments.
        
        :param name: The name of the function to execute.
        :type name: str
        :param args: The arguments to pass to the function.
        :type args: dict
        :return: The result of the function's execution, which should be a string with the response for the user (it can also be a dictionary in certain cases).
        :rtype: str | dict
        """