from ..config.config import ModuleLoader
from ..interfaces.llm_adapter_interface import LLMAdapter
from ..utils.system_prompt_generator import AssistantSystemPromptGenerator
from .assistant_backend import AssistantBackend
from ..utils.function_handler import AssistantFunctionHandler
from ..ui.assistant_gui import AssistantGUI
from ..ui.chat_handler import AssistantChatHandler
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def main():
    module_loader = ModuleLoader()
    # Load functionality modules
    functionality_modules = module_loader.load_functionality_modules()
    # Initialize the system prompt and backend
    prompt = AssistantSystemPromptGenerator(functionality_modules).generate()
    print("====== \n" + prompt + "\n======")
    llm_model_name = module_loader.get_llm_model()
    llm_adapter: LLMAdapter = module_loader.load_base_module("llm", model=llm_model_name, prompt=prompt)
    backend = AssistantBackend(llm_adapter, AssistantFunctionHandler(functionality_modules))
    # Initialize the GUI & Chat Handler
    chat_handler = AssistantChatHandler(backend, module_loader.load_base_module("ss"), module_loader.load_base_module("sr"))
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = AssistantGUI(chat_handler)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__": main()