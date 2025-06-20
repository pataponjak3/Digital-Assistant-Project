def generate_llama_system_prompt(modules: dict) -> str:
    # def describe_properties(properties: dict, indent: int = 0) -> str:
    #     result = ""
    #     for key, value in properties.items():
    #         desc = value.get("description", "No description")
    #         type_ = value.get("type", "unknown")
    #         spacing = "  " * indent
    #         result += f"{spacing}- {key} ({type_}): {desc}\n"
    #         if type_ == "array" and "items" in value:
    #             items = value["items"]
    #             item_type = items.get("type", "unknown")
    #             result += f"{spacing}  [Array of {item_type}]:\n"
    #             if "properties" in items:
    #                 result += describe_properties(items["properties"], indent + 2)
    #         elif "properties" in value:
    #             result += describe_properties(value["properties"], indent + 1)
    #     return result
    
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

    for module in modules.values():
        for func in module.get_functions_description():
            prompt += func + "\n\n"
    
    prompt += (
        "Only respond with a JSON object when the user’s message clearly requires calling a function (like requesting weather or pollution data). "
        "For example, \"What’s the weather in Lisbon?\" would match a function.\n\n"
        "If the user refers to earlier data or asks follow-up questions about information you already returned (e.g., “What can you tell me about this data?”), answer NATURALLY and DO NOT generate a JSON object.\n\n"
        "Never reflect on how you should have responded. Focus on answering the user’s latest question or request clearly and helpfully, using the information you already provided if relevant."
    )

    # prompt = (
    #     "You are a digital assistant that can call predefined functions.\n\n"
    #     "IMPORTANT:\n"
    #     "- If the user's input matches one of the listed functions, you MUST reply with ONLY a JSON object in this exact format:\n"
    #     "{\n"
    #     '  "module": "<module_name>",\n'
    #     '  "function": "<function_name>",\n'
    #     '  "arguments": { "key": "value" }\n'
    #     "}\n"
    #     "IMPORTANT: Always respond ONLY with a JSON object for function calls. Never say 'I'm a large language model' or similar. If you cannot find a function, respond with 'No function match.' Nothing else."
    #     "- Do NOT write anything else before or after the JSON.\n"
    #     "- If the user's input does not match any function, then reply in plain natural language.\n"
    #     "\nAvailable functions:\n"
    # )

    # for module in modules.values():
    #     for func in module.get_functions_schemas():
    #         name = func.get("name", "unknown")
    #         module = func.get("module", "unknown")
    #         desc = func.get("description", "No description")
    #         response_fmt = ", ".join(func.get("response_format", []))

    #         prompt += f"\nFunction: {name}\nModule: {module}\nDescription: {desc}\nResponse Format: {response_fmt}\n"

    #         # Parameters section
    #         params = func.get("parameters", {})
    #         if params:
    #             param_desc = params.get("description", "")
    #             if param_desc:
    #                 prompt += f"Parameters Description: {param_desc}\n"
    #             if "properties" in params:
    #                 prompt += "Parameters:\n" + describe_properties(params["properties"])
    #         else:
    #             prompt += "Parameters: None\n"

    #         # Response Schema section
    #         response_schema = func.get("response_schema", {})
    #         if response_schema:
    #             for fmt, schema in response_schema.items():
    #                 prompt += f"Response Fields ({fmt}):\n" + describe_properties(schema.get("properties", {}))
    #         else:
    #             prompt += "Response Fields: None\n"
            

    #     prompt += (
    #     "\nRemember:\n"
    #     "- Always respond with JSON ONLY when a function applies.\n"
    #     "- Otherwise, respond naturally.\n\n"
    #     "Here are some examples of correct behavior:\n\n"
    #     "Example 1:\n"
    #     "User: What is the weather like in Lisbon?\n"
    #     "Assistant:\n"
    #     "{\n"
    #     '  "module": "meteorology",\n'
    #     '  "function": "get_current_weather",\n'
    #     '  "arguments": {\n'
    #     '    "city": "Lisbon"\n'
    #     "  }\n"
    #     "}\n\n"
    #     "Example 2:\n"
    #     "User: Can you tell me the forecast for Porto?\n"
    #     "Assistant:\n"
    #     "{\n"
    #     '  "module": "meteorology",\n'
    #     '  "function": "get_forecast",\n'
    #     '  "arguments": {\n'
    #     '    "city": "Porto"\n'
    #     "  }\n"
    #     "}\n\n"
    #     "Example 3:\n"
    #     "User: I want to know the air pollution levels in Faro.\n"
    #     "Assistant:\n"
    #     "{\n"
    #     '  "module": "meteorology",\n'
    #     '  "function": "get_air_pollution",\n'
    #     '  "arguments": {\n'
    #     '    "city": "Faro"\n'
    #     "  }\n"
    #     "}\n\n"
    #     "IMPORTANT: Always follow the examples. Do not add explanations, headers, or extra text when using JSON.\n"
    # )

    return prompt
