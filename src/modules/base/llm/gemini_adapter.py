import json

from openai import OpenAI #Although this module utilizes a REST API, we use the official OpenAI Python client for simplicity.
from ....config.config import APIKeyManager
from ....interfaces.llm_adapter_interface import LLMAdapter
from typing import Optional

class GeminiAdapter(LLMAdapter):
    __client = OpenAI(
        api_key = APIKeyManager().get_key("gemini"),
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    def __init__(self, model: str, prompt: str, tools: Optional[list]=None):
        self.__model = model
        self.__system_prompt = prompt
        self.__tools = tools if tools is not None else []
        self.__messages = [{"role": "system", "content": self.__system_prompt}]

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

            try:
                result = self.__client.chat.completions.create(
                    model=self.__model,
                    temperature=0.7,
                    top_p=0.9,
                    max_completion_tokens=1024,
                    messages=self.__messages
                )


                input = result.choices[0].message.content

            except Exception as e:
                print(f"ERROR: Gemini chat call failed: {e}")
                return "I’m having trouble generating a response right now."
            

        # Add assistant message to conversation history, but not function calls
        if not is_json(input):
            self.__messages.append({"role": "assistant", "content": input})

        return input
        
    
