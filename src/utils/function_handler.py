from ..interfaces.functionality import Functionality

class FunctionHandler:
    def __init__(self, modules: dict):
        self.__modules = modules

    def call_function(self, module_name: str, function_name: str, arguments: dict) -> str:
        module: Functionality = self.__modules.get(module_name)
        if not module:
            return "Module not found"
        return module.execute_function(function_name, arguments)