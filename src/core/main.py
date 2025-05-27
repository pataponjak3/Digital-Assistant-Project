#from ..ui.gui import AssistantGUI
from .config import ModuleLoader, APIKeyManager
import sys
from ..ui.assistant_interface import AssistantGUI
from PyQt5.QtWidgets import QApplication, QMainWindow
import json
from ..modules.fn.met.meteorology import MeteorologyService
from ..utils.system_prompt_generator import generate_llama_system_prompt

def main():
    #module_loader = ModuleLoader()
    api_key_manager = APIKeyManager()
    #app = QApplication(sys.argv)
    #MainWindow = QMainWindow()
    #ui = AssistantGUI(module_loader)
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())
    modules = {
        "meteorology": MeteorologyService(api_key_manager.get_key("openweathermap"))
    }
    print(generate_llama_system_prompt(modules))


if __name__ == "__main__": main()

def handle_user_message(llm_adapter, modules, user_input):
    # Step 1: Send message to LLM
    messages = [{"role": "user", "content": user_input}]
    response = llm_adapter.chat(messages)

    # Step 2: Check if response is a function call
    try:
        parsed = json.loads(response["content"])
        if "function" in parsed and "arguments" in parsed:
            func_name = parsed["function"]
            args = parsed["arguments"]

            # Step 3: Find and call correct function
            for module in modules.values():
                if hasattr(module, "execute_function_call"):
                    try:
                        result = module.execute_function_call(func_name, args)
                        # Step 4: Send result back to LLM for final response
                        result_message = [
                            {"role": "user", "content": user_input},
                            {"role": "assistant", "content": json.dumps(parsed)},
                            {"role": "function", "content": json.dumps(result)}
                        ]
                        final_response = llm_adapter.chat(result_message)
                        return final_response["content"]
                    except Exception as e:
                        return f"Error executing function: {e}"
        else:
            # If no function call, return as natural response
            return response["content"]
    except json.JSONDecodeError:
        # Fallback: treat as natural response
        return response["content"]