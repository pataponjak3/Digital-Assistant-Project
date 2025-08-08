from abc import ABC, abstractmethod

class FunctionHandler(ABC):

    @abstractmethod
    def call_function(self, module_name: str, function_name: str, arguments: dict) -> str:
        """
        Call a function from a specific module with the given arguments.

        :param module_name: Name of the module containing the function.
        :type module_name: str
        :param function_name: Name of the function to call.
        :type function_name: str
        :param arguments: Arguments to pass to the function.
        :type arguments: dict
        :return: Result of the function call, which should be a string containing the response for the user.
        :rtype: str
        """
        pass
        