from abc import ABC, abstractmethod

class DAFunctionalityInterface(ABC):
    """Interface for functionalities of the DA"""

    @abstractmethod
    def get_functions_schemas(self) -> list[dict]:
        """Definition of the functions' schemas.
        This is an important part of each functionality, because this will demonstrate to the DA how the function works.

        :return: A list of dictionaries, each containing the schema of a function.
        """
    
    @abstractmethod
    def execute_function(self, name:str, args:dict):
        """Execute the function with the given name and arguments.
        
        :param name: The name of the function to execute.
        :param args: The arguments to pass to the function.
        :return: The result of the function execution.
        """