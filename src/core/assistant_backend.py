from ..interfaces.llm_adapter_interface import LLMAdapter
from ..interfaces.backend_interface import Backend
from ..interfaces.func_handler_interface import FunctionHandler
import json

class AssistantBackend(Backend):
    def __init__(self, llm_adapter: LLMAdapter, function_handler: FunctionHandler):
        self.__llm = llm_adapter
        self.__function_handler = function_handler

    def _llm_adapter(self) -> LLMAdapter:
        return self.__llm
    
    def _function_handler(self) -> FunctionHandler:
        return self.__function_handler

    def handle_user_message(self, user_message: str) -> str:
        try:
            response = self.__llm.chat(user_message)

            try:
                call = json.loads(response)
                if "function" in call and "arguments" in call:
                    try:
                        message = self.__function_handler.call_function(call["module"], call["function"], call["arguments"])
                        print("I executed call function")
                        final_response = self.__llm.chat(message, False)
                        return final_response
                    except Exception as e:
                        return f"Error executing function: {e}"
                else:
                    # Not a function call, return as-is
                    return response

            except json.JSONDecodeError:
                # Not JSON, return as-is
                return response

        except Exception as e:
            return f"Error: {e}"
