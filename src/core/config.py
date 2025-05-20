import importlib
import json
import os

class ModuleLoader:
    def __init__(self, config_path="config.json"):
        with open(os.path.abspath(config_path), "r") as file:
            self.config = json.load(file)

    def load_module(self, module_name: str):
        module_info = self.config.get(module_name)
        if not module_info:
            raise ValueError(f"No implementation specified for {module_name} in config.")
        file_path = module_info.get("filePath")
        class_name = module_info.get("class")
        if not file_path or not class_name:
            raise ValueError(f"Misssing file path or class name for {module_name}")
        try:
            module = importlib.import_module(f"src.modules.{file_path}")
            return getattr(module, class_name)()
        except ModuleNotFoundError:
            raise ImportError(f"Module 'src.modules.{file_path}' not found!")
        except AttributeError:
            raise ImportError(f"Class {class_name} not found in {file_path}!")

class APIKeyManager:
    def __init__(self, config_path="config.json"):
        self._keys = {}
        self._load_keys(config_path)
    
    def _load_keys(self, config_path: str):
        try:
            with open(os.path.abspath(config_path), "r") as file:
                config = json.load(file)
                self._keys = config.get("apiKeys", {}) #Optional
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading API keys: {e}")
        
    def get_key(self, service_name:str) -> str:
        key = self._keys.get(service_name.lower())
        if not key:
            raise ValueError(f"No API key found for {service_name}")
        return key 