import importlib
import json
import os

class ModuleLoader:
    def __init__(self, config_path="config.json"):
        with open(os.path.abspath(config_path), "r") as file:
            self.config = json.load(file)

    def load_module(self, module_name):
        module_info = self.config.get(module_name)
        if not module_info:
            raise ValueError(f"No implementation specified for {module_name}")
        file_name = module_info.get("file")
        class_name = module_info.get("class")
        if not file_name or not class_name:
            raise ValueError(f"Misssing file or class name for {module_name}")
        try:
            module = importlib.import_module(f"src.modules.{module_name}.{file_name}")
            return getattr(module, class_name)()
        except ModuleNotFoundError:
            raise ImportError(f"Implementation {file_name} for {module_name} not found!")
        except AttributeError:
            raise ImportError(f"Class {class_name} not found in {file_name}!")