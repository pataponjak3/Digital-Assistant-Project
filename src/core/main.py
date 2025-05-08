#from ..ui.gui import AssistantGUI
from .config import ModuleLoader
import sys
from ..ui.assistant_interface import AssistantGUI
from PyQt5.QtWidgets import QApplication, QMainWindow

def main():
    #print("Launching Digital Assistant GUI...")
    #AssistantGUI()
    module_loader = ModuleLoader()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = AssistantGUI(module_loader)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__": main()