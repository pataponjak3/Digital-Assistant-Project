#from ..ui.gui import AssistantGUI
from ..config.config import ModuleLoader
from ..utils.system_prompt_generator import SystemPromptGenerator
from ..core.backend import AssistantBackend
from ..utils.function_handler import FunctionHandler
from ..ui.assistant_gui import AssistantGUI
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def main():
    module_loader = ModuleLoader()
    # Load functionality modules
    functionality_modules = module_loader.load_functionality_modules()
    # Initialize the system prompt and backend
    prompt = SystemPromptGenerator(functionality_modules).generate()
    llm_model_name = module_loader.get_llm_model()
    llm_adapter = module_loader.load_base_module("llm", model=llm_model_name, prompt=prompt)
    backend = AssistantBackend(llm_adapter, FunctionHandler(functionality_modules))
    # Initialize the GUI
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = AssistantGUI(module_loader, backend)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__": main()