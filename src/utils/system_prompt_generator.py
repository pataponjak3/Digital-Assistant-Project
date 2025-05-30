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
        "You are a helpful digital assistant. When a task requires a specific function, "
        "reply in JSON format like this:\n"
        "{\n"
        '  "function": "<function_name>",\n'
        '  "module": "<module_name>",\n'
        '  "arguments": { "key": "value" }\n'
        "}\n\n"
        "Functions you can call:\n"
    )

    for module in modules.values():
        for func in module.get_functions_schemas():
            name = func.get("name", "unknown")
            module = func.get("module", "unknown")
            desc = func.get("description", "No description")
            response_fmt = ", ".join(func.get("response_format", []))

            prompt += f"\nFunction: {name}\nModule: {module}\nDescription: {desc}\nResponse Format: {response_fmt}\n"

            # Parameters section
            params = func.get("parameters", {})
            if params and "properties" in params:
                prompt += "Parameters:\n" + describe_properties(params["properties"])
            else:
                prompt += "Parameters: None\n"

            # Response Schema section
            response_schema = func.get("response_schema", {})
            if response_schema:
                for fmt, schema in response_schema.items():
                    prompt += f"Response Fields ({fmt}):\n" + describe_properties(schema.get("properties", {}))
            else:
                prompt += "Response Fields: None\n"
            

    prompt += (
        "\nIf the user's request doesn't match any function, just answer naturally in plain text.\n"
        "When calling a function, only reply with the JSON object. No extra explanation.\n"
    )

    return prompt
