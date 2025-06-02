def generate_llama_system_prompt(modules: dict) -> str:
    def describe_properties(properties: dict, indent: int = 0) -> str:
        result = ""
        for key, value in properties.items():
            desc = value.get("description", "No description")
            type_ = value.get("type", "unknown")
            spacing = "  " * indent
            result += f"{spacing}- {key} ({type_}): {desc}\n"
            if type_ == "array" and "items" in value:
                items = value["items"]
                item_type = items.get("type", "unknown")
                result += f"{spacing}  [Array of {item_type}]:\n"
                if "properties" in items:
                    result += describe_properties(items["properties"], indent + 2)
            elif "properties" in value:
                result += describe_properties(value["properties"], indent + 1)
        return result
    
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
        "\nAvailable functions:\n"
        "Function: get_current_weather\n"
        "Module: meteorology\n"
        "Description: Get the current weather for a location.\n"
        "Arguments:\n"
        "- city (string): City name. Optionally add state_code and country_code.\n"
        "- lat (number) and lon (number): Coordinates.\n"
        "- zip (string) and country_code (string): Postal code and country.\n\n"
        "Function: get_forecast\n"
        "Module: meteorology\n"
        "Description: Get a 5-day forecast in 3-hour intervals.\n"
        "Arguments: Same as get_current_weather.\n\n"
        "Function: get_air_pollution\n"
        "Module: meteorology\n"
        "Description: Get current air pollution data for a location.\n"
        "Arguments: Same as get_current_weather.\n\n"
        "Always respond with the JSON format for functions, and nothing else."
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
