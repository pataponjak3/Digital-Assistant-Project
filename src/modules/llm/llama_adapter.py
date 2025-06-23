import requests
import json

from ...config.config import APIKeyManager

class AwanLlamaAdapter:
    def __init__(self, model: str, prompt: str):
        self.api_key = APIKeyManager().get_key("awanllm")
        self.model = model
        self.system_prompt = prompt
        print("=====" + self.system_prompt)
        self.api_url = "https://api.awanllm.com/v1/chat/completions"
        self.messages = [{"role": "system", "content": self.system_prompt}]  # Initial conversation history

    def chat(self, input: str, user_message=True) -> str:
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