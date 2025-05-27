import requests
import os
from ...interfaces.llm_adapter import LLMAdapterInterface

class LLaMAAdapter(LLMAdapterInterface):
    def __init__(self, modules: dict, api_key=None, model="Meta-Llama-3.1-8B-Instruct"):
        self.api_key = api_key or os.getenv("AWAN_API_KEY")
        self.model = model
        self.endpoint = "https://api.awanllm.com/v1/chat/completions"
        self.modules = modules

    def chat(self, messages: list[dict], functions: list[dict] = None) -> dict:
        # Generate dynamic system prompt
        #system_prompt = generate_llama_system_prompt(self.modules)

        # Inject system prompt at the top of the messages
        messages = [{"role": "system", "content": system_prompt}] + messages

        payload = {
            "model": self.model,
            "messages": messages
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(self.endpoint, json=payload, headers=headers)
        response.raise_for_status()

        return response.json()["choices"][0]["message"]

    def get_provider_name(self) -> str:
        return "Awan LLaMA"
