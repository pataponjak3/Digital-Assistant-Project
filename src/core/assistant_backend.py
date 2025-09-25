from interfaces.llm_adapter_interface import LLMAdapter
from interfaces.backend_interface import Backend
from interfaces.func_handler_interface import FunctionHandler

class AssistantBackend(Backend):
    def __init__(self, llm_adapter: LLMAdapter, function_handler: FunctionHandler, supports_function_calls: bool=False):
        self.__llm = llm_adapter
        self.__function_handler = function_handler
        self.__supports_function_calls = supports_function_calls

    def _llm_adapter(self) -> LLMAdapter:
        return self.__llm
    
    def _function_handler(self) -> FunctionHandler:
        return self.__function_handler

    def handle_user_message(self, user_message: str) -> str:
        try:
            response = self.__llm.chat(user_message, True, self.__supports_function_calls)

            if response.type == "function_call":
                try: 
                    message = self.__function_handler.call_function(response.module, response.function, response.arguments, self.__supports_function_calls)
                    final_response = self.__llm.chat(message, False, self.__supports_function_calls)
                    return final_response.content
                    #if isinstance(message, FunctionalityReturn):
                    #    # Log raw for testing if available
                    #    if message.get("raw") is not None:
                    #        self._log_raw_response(message["raw"])

                    #    if self.__supports_function_calls:
                    #        # Pass raw JSON if available, else fallback to formatted
                    #        llm_input = message["raw"] if message.get("raw") else message["formatted"]
                    #        final_response = self.__llm.chat(llm_input, False, self.__supports_function_calls)
                    #        return final_response.content
                    #    else:
                    #        return message["formatted"]

                    #else:
                    #    # Legacy fallback (plain string return)
                    #    final_response = self.__llm.chat(str(message), False, self.__supports_function_calls)
                    #    return final_response.content
                except Exception as e:
                    return f"Error executing function: {e}"
            else:
                return response.content

        except Exception as e:
            return f"Error: {e}"
