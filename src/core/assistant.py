import json

def handle_user_message(llm_adapter, modules: dict, user_input: str) -> str:
    try:
        llm_response = llm_adapter.chat(user_input)

        try:
            parsed = json.loads(llm_response)
            if "function" in parsed and "arguments" in parsed:
                func_name = parsed["function"]
                module_name = parsed["module"]
                args = parsed["arguments"]

                module = modules.get(module_name)

                try:
                    result = module.execute_function_call(func_name, args)
                    final_response = llm_adapter.chat(json.dumps(result))
                    return final_response
                except Exception as e:
                    return f"Error executing function: {e}"
            else:
                # Not a function call, return natural response
                return llm_response

        except json.JSONDecodeError:
            # Not JSON, return as-is
            return llm_response

    except Exception as e:
        return f"Error: {e}"
