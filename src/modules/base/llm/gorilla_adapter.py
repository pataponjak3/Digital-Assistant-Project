import json

from openai import OpenAI #Although this module utilizes a REST API, we use the official OpenAI Python client for simplicity.
from config.config import APIKeyManager
from interfaces.llm_adapter_interface import LLMAdapter
from app_types.app_types import LLMResponse
from typing import Optional

class GorillaAdapter(LLMAdapter):
    __client = OpenAI(
        api_key = APIKeyManager().get_key("gorilla"),
        base_url = "http://luigi.millennium.berkeley.edu:8000/v1"
    )

    def __init__(self, model: str, prompt: str, tools: Optional[list]=None):
        self.__model = model
        self.__system_prompt = prompt
        self.__tools = tools if tools is not None else []
        self.__messages = [{"role": "system", "content": self.__system_prompt}]

    def chat(self, input: str, is_not_da_response: bool=True, supports_function_calls: bool=False) -> LLMResponse:
            
        if is_not_da_response:
            self.__messages.append({"role": "user", "content": input})

            try:
                result = self.__client.chat.completions.create(
                    model=self.__model,
                    temperature=0.7,
                    top_p=0.9,
                    messages=self.__messages,
                    functions=self.__tools if supports_function_calls else None,
                    tool_choice="auto" if (supports_function_calls and self.__tools) else "none"
                )
            except Exception as e:
                print(f"ERROR: Gorilla chat call failed: {e}")
                return LLMResponse(type="response", content="I’m having trouble generating a response right now.")
            
            choice = result.choices[0].message

            # --- A) Structured function call (tool_calls present) ---
            if supports_function_calls and choice.function_call:
                self.__messages.append(choice) # Store da tool calls in message history
                module_name, function_name = choice.function_call.name.split("_", 1)
                args = choice.function_call.arguments
                # Do NOT append assistant/tool message yet, Backend will push result
                return LLMResponse(
                    type="function_call",
                    function=function_name,
                    module=module_name,
                    arguments=args
                )

            # --- B) Text-based JSON function call ---
            if choice.content:
                try:
                    raw_content = choice.content.strip()
                    if raw_content.startswith("```"):
                        # Remove first line (```json or ```)
                        lines = raw_content.splitlines()
                        if lines[0].startswith("```"):
                            lines = lines[1:]
                        if lines and lines[-1].startswith("```"):
                            lines = lines[:-1]
                        raw_content = "\n".join(lines).strip()
                    parsed = json.loads(raw_content)
                    if "function" in parsed and "arguments" in parsed:
                        return LLMResponse(
                            type="function_call",
                            function=parsed["function"],
                            module=parsed["module"],
                            arguments=parsed["arguments"]
                        )
                except json.JSONDecodeError:
                    pass

                # --- C) Normal assistant response ---
                self.__messages.append({"role": "assistant", "content": choice.content})
                return LLMResponse(type="response", content=choice.content)

            # If no content, return fallback
            return LLMResponse(type="response", content="I did not receive any response. Please try again.")
        
        else:
            if supports_function_calls:
                self.__messages.append({"role": "user", "content": input})
                try:
                    result = self.__client.chat.completions.create(
                        model=self.__model,
                        temperature=0.7,
                        top_p=0.9,
                        messages=self.__messages,
                        tools=self.__tools if supports_function_calls else None,
                        tool_choice="auto" if (supports_function_calls and self.__tools) else "none"   
                    )
                except Exception as e:
                    print(f"ERROR: Gorilla chat call failed after tool input: {e}")
                    return LLMResponse(type="response", content=f"There was an error generating a response: {e}")

                print(result)
                choice = result.choices[0].message
                self.__messages.append({"role": "assistant", "content": choice.content})
                return LLMResponse(type="response", content=choice.content)
            else:
                # No function calling support → just store result as assistant response
                self.__messages.append({"role": "assistant", "content": input})
                return LLMResponse(type="response", content=input)
            
    def clear_chat_history(self):
        self.__messages = [{"role": "system", "content": self.__system_prompt}]  # Initial conversation history