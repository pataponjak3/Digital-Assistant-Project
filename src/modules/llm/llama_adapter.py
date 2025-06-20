import requests
import json

from ...core.config import APIKeyManager
from ...utils.system_prompt_generator import generate_llama_system_prompt

class AwanLlamaAdapter:
    def __init__(self, model: str, functionality_modules: dict):
        self.api_key = APIKeyManager().get_key("awanllm")
        self.model = model
        self.functionality_modules = functionality_modules
        self.system_prompt = generate_llama_system_prompt(functionality_modules)
        print("=====" + self.system_prompt)
        self.api_url = "https://api.awanllm.com/v1/chat/completions"
        self.messages = [{"role": "system", "content": self.system_prompt}]  # Initial conversation history

    def chat(self, input: str, user_message: bool) -> str:
        def is_json(text):
            try:
                json.loads(text)
                return True
            except (ValueError, TypeError):
                return False
        
        if user_message:
            # Add user message to conversation history
            print("=====" + input)
            self.messages.append({"role": "user", "content": input})

            payload = {
                "model": self.model,
                "messages": self.messages,
                "temperature": 0.7,
                "top_p": 0.9,
                "repetition_penalty": 1.1,
                "top_k": 40,
                "max_tokens": 1024,
                "stream": False
            }

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {self.api_key}"
            }

            response = requests.post(self.api_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()

            result = response.json()
            print("===== result =====" + str(result))
            input = result["choices"][0]["message"]["content"]

        # Add assistant message to conversation history
        if not is_json(input):
            self.messages.append({"role": "assistant", "content": input})

        print("=====" + input)

        return input
    
    def handle_user_message(self, user_input: str) -> str:
        try:
            llm_response = self.chat(user_input, True)

            try:
                parsed = json.loads(llm_response)
                if "function" in parsed and "arguments" in parsed:
                    func_name = parsed["function"]
                    module_name = parsed["module"]
                    args = parsed["arguments"]

                    module = self.functionality_modules.get(module_name)

                    try:
                        message = module.execute_function(func_name, args)
                        final_response = self.chat(message, False)
                        return final_response
                    except Exception as e:
                        return f"Error executing function: {e}"
                else:
                    # Not a function call, return natural response
                    return llm_response

            except json.JSONDecodeError:
                # Not JSON, return as-is
                return llm_response

        except Exception as e:
            return f"Error: {e}"