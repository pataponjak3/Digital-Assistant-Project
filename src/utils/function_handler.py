from ..interfaces.functionality_interface import Functionality
from ..interfaces.func_handler_interface import FunctionHandler

class AssistantFunctionHandler(FunctionHandler):
    def __init__(self, modules: dict[str, Functionality]):
        self.__modules = modules
    
    def _modules(self):
        return self.__modules

    def call_function(self, module_name: str, function_name: str, arguments: dict):
        module: Functionality = self.__modules.get(module_name)
        if not module:
            return "Module not found"
        return module.execute_function(function_name, arguments)