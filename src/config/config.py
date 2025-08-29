import importlib
import json
import os
from dotenv import load_dotenv
from ..interfaces.functionality_interface import Functionality
from .modules import LLM_REGISTRY
from typing import Type, Any

class ModuleLoader:
    def __init__(self, config_path="src/config/config.json"):
        with open(os.path.abspath(config_path), "r") as file:
            self.__config: dict = json.load(file)

        llm_name = self.__config["modules"]["base"]["llm"]["model"]

        if llm_name in LLM_REGISTRY:
            self.__config["modules"]["base"]["llm"] = LLM_REGISTRY[llm_name]
        else:
            raise ValueError(f"Unknown LLM model: {llm_name}")

    def _load_module(self, config_part: dict, module_name: str, **kwargs) -> Type:
        module_info = config_part.get(module_name)
        if not module_info:
            raise ValueError(f"No implementation specified for {module_name} in config.")
        file_path = module_info.get("filePath")
        print(f"====={file_path}")
        class_name = module_info.get("class")
        print(f"====={class_name}")
        if not file_path or not class_name:
            raise ValueError(f"Misssing file path or class name for {module_name}")
        try:
            module = importlib.import_module(f"src.modules.{file_path}")
            print("=====" + module.__name__)
            return getattr(module, class_name)(**kwargs)
        except ModuleNotFoundError:
            raise ImportError(f"Module 'src.modules.{file_path}' not found!")
        except AttributeError:
            raise ImportError(f"Class {class_name} not found in {file_path}!")
    
    def load_functionality_modules(self) -> dict[str, Functionality]:
        modules = {}
        modules_info = self.__config.get("modules").get("fn", {})
        for module_name in modules_info:
            try:
                modules[module_name] = self._load_module(modules_info, module_name)
                print("=====" + module_name)
            except (ValueError, ImportError) as e:
                print(f"Error loading module {module_name}: {e}")
        return modules
    
    def load_base_module(self, module_name, **kwargs):
        base_modules = self.__config.get("modules").get("base")
        if module_name not in base_modules:
            raise ValueError(f"Base module {module_name} not found in config.")
        return self._load_module(base_modules, module_name, **kwargs)
    
    def get_llm_model(self) -> str:
        llm_config = self.__config.get("modules").get("base").get("llm")
        if not llm_config:
            raise ValueError("LLM configuration not found in config.")
        return llm_config.get("model", "default_model")


class APIKeyManager:
    def __init__(self, env_path=".env"):
        load_dotenv(dotenv_path=env_path)
        
    def get_key(self, service_name:str) -> str:
        env_var = f"{service_name.upper()}_KEY"
        key = os.getenv(env_var)

        if not key:
            raise ValueError(f"No API key found for {service_name} (expected {env_var})")

        return key