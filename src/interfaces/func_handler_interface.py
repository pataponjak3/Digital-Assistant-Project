from abc import ABC, abstractmethod
from interfaces.functionality_interface import Functionality
from typing import Callable

class FunctionHandler(ABC):

    @property
    @abstractmethod
    def _modules(self) -> dict[str, Functionality]:
        """
        Dictionary of modules available for function calls.

        :return: Dictionary mapping module names to Functionality instances.
        :rtype: dict[str, Functionality]
        """
        pass

    @abstractmethod
    def call_function(self, module_name: str, function_name: str, arguments: dict, supports_function_calls: bool) -> Callable[[str, dict], Callable[[dict], str | dict]]:
        """
        Call a function from a specific module with the given arguments.

        :param module_name: Name of the module containing the function.
        :type module_name: str
        :param function_name: Name of the function to call.
        :type function_name: str
        :param arguments: Arguments to pass to the function.
        :type arguments: dict
        :return: Result of the function call, which should be string with the response for the user (it can also be a dictionary in certain cases).
        :rtype: str | dict
        """
        pass
        