#from ..ui.gui import AssistantGUI
from .config import ModuleLoader, APIKeyManager
import sys
from ..ui.assistant_interface import AssistantGUI
from PyQt5.QtWidgets import QApplication, QMainWindow
from .assistant import handle_user_message

def main():
    module_loader = ModuleLoader()
    api_key_manager = APIKeyManager()
    #app = QApplication(sys.argv)
    #MainWindow = QMainWindow()
    #ui = AssistantGUI(module_loader)
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())
    modules = module_loader.load_functionality_modules()

    llm_adapter = module_loader.load_base_module("llm", model=module_loader.get_llm_model(), modules=modules)

    print("Digital Assistant is ready!")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = handle_user_message(llm_adapter, modules, user_input)
        print("DA:", response)

if __name__ == "__main__": main()