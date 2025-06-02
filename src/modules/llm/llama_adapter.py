import requests
import json

from ...core.config import APIKeyManager
from ...utils.system_prompt_generator import generate_llama_system_prompt

class AwanLlamaAdapter:
    def __init__(self, model: str, modules: dict):
        self.api_key = APIKeyManager().get_key("awanllm")
        self.model = model
        self.system_prompt = generate_llama_system_prompt(modules)
        print("=====" + self.system_prompt)
        self.api_url = "https://api.awanllm.com/v1/chat/completions"
        self.messages = [{"role": "system", "content": self.system_prompt}]  # Initial conversation history

    def chat(self, user_input: str) -> str:
        # Add user message to conversation history
        print("=====" + user_input)
        self.messages.append({"role": "user", "content": user_input})

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
        print("=====" + str(result))
        assistant_message = result["choices"][0]["message"]["content"]

        # Add assistant message to conversation history
        self.messages.append({"role": "assistant", "content": assistant_message})

        print(assistant_message)

        return assistant_message