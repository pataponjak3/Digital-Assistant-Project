from ..interfaces.llm_adapter import LLMAdapter
import json

class AssistantBackend:
    def __init__(self, llm_adapter: LLMAdapter, function_handler):
        self.__llm = llm_adapter
        self.__functions = function_handler

    def handle_user_message(self, user_message: str) -> str:
        try:
            response = self.__llm.chat(user_message)

            try:
                call = json.loads(response)
                if "function" in call and "arguments" in call:
                    try:
                        message = self.__functions.call_function(call["module"], call["function"], call["arguments"])
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
