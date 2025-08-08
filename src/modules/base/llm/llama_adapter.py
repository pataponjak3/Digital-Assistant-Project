import requests
import json

from ....config.config import APIKeyManager
from ....interfaces.llm_adapter_interface import LLMAdapter
from ....interfaces.rest_service_interface import RESTService

class AwanLlamaAdapter(RESTService, LLMAdapter):
    __base_url = "https://api.awanllm.com"
    __api_key = APIKeyManager().get_key("awanllm")
    __chat_completions_endpoint = "v1/chat/completions"

    def __init__(self, model: str, prompt: str):
        self.__model = model
        self.__system_prompt = prompt
        self.__messages = [{"role": "system", "content": self.__system_prompt}]  # Initial conversation history
        print("=====" + self.__system_prompt + "\n=====" + self.__model)

    def _base_url(self):
        return self.__base_url
    
    def _api_key(self):
        return self.__api_key

    def _send_resquest(self, method:str, endpoint: str, **kwargs) -> dict:
        headers = kwargs.get('headers')
        data = kwargs.get('data')

        response = requests.request(
            method=method,
            url=f"{self.__base_url}/{endpoint}",
            headers=headers,
            data=data
        )
        
        response.raise_for_status()
        return response.json()


    def chat(self, input: str, is_user_message: bool=True) -> str:
        def is_json(text):
            try:
                json.loads(text)
                return True
            except (ValueError, TypeError):
                return False
        
        if is_user_message:
            # Add user message to conversation history
            print("=====" + input)
            self.__messages.append({"role": "user", "content": input})

            payload = {
                "model": self.__model,
                "messages": self.__messages,
                "temperature": 0.7,
                "top_p": 0.9,
                "repetition_penalty": 1.1,
                "top_k": 40,
                "max_tokens": 1024,
                "stream": False
            }

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"Bearer {self.__api_key}"
            }

            result = self._send_resquest("POST", self.__chat_completions_endpoint, headers=headers, data=json.dumps(payload))
            
            print("===== result =====" + str(result))
            input = result["choices"][0]["message"]["content"]

        # Add assistant message to conversation history
        if not is_json(input):
            self.__messages.append({"role": "assistant", "content": input})

        print("=====" + input)

        return input