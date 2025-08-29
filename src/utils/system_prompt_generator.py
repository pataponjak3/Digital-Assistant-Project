from ..interfaces.functionality_interface import Functionality
from ..interfaces.sys_prompt_interface import SystemPromptGenerator

class AssistantSystemPromptGenerator(SystemPromptGenerator):
    def __init__(self, modules: dict[str, Functionality]):
        self.__modules = modules
    
    def _modules(self) -> dict[str, Functionality]:
        return self.__modules
        
    def generate(self) -> str:
        prompt = (
            "You are a digital assistant that can call predefined functions when they match the user's request.\n\n"
            "IMPORTANT RULES:\n"
            "- If the user’s input matches a function, reply ONLY with a JSON object in this format:\n"
            "{\n"
            '  "module": "<module_name>",\n'
            '  "function": "<function_name>",\n'
            '  "arguments": { "key": "value" }\n'
            "}\n"
            "Do not include explanations, disclaimers, or any other text.\n"
            "- If the user’s input does NOT match a function, reply naturally.\n"
            "\nAvailable functions:\n\n"
        )

        module: Functionality
        for module in self.__modules.values():
            for func in module.get_functions_description():
                prompt += func + "\n\n"
        
        prompt += (
            "Only respond with a JSON object when the user’s message clearly requires calling a function (like requesting weather or pollution data). "
            "For example, \"What’s the weather in Lisbon?\" would match a function.\n\n"
            "If the user refers to earlier data or asks follow-up questions about information you already returned (e.g., “What can you tell me about this data?”), answer NATURALLY and DO NOT generate a JSON object.\n\n"
            "Never reflect on how you should have responded. Focus on answering the user’s latest question or request clearly and helpfully, using the information you already provided if relevant."
        )

        return prompt
