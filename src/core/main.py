#from ..ui.gui import AssistantGUI
from .config import ModuleLoader, APIKeyManager
import sys
from ..ui.assistant_interface import AssistantGUI
from PyQt5.QtWidgets import QApplication, QMainWindow

def main():
    app = QApplication(sys.argv)
    module_loader = ModuleLoader()
    llm_adapter = module_loader.load_base_module("llm", model=module_loader.get_llm_model(), functionality_modules=module_loader.load_functionality_modules())
    MainWindow = QMainWindow()
    ui = AssistantGUI(module_loader, llm_adapter)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__": main()