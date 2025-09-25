LLM_REGISTRY = {
    "Awan-Llama-3.1-8B-Instruct": {
        "filePath": "base.llm.awan_llama_adapter",
        "class": "AwanLlamaAdapter",
        "model": "Meta-Llama-3.1-8B-Instruct",
        "suportsFunctionCalls": False
    },
    "Gemini-2.0-Flash": {
        "filePath": "base.llm.gemini_adapter",
        "class": "GeminiAdapter",
        "model": "gemini-2.0-flash",
        "suportsFunctionCalls": False
    },
    "Gorilla-OpenFunctions-v2": {
        "filePath": "base.llm.gorilla_adapter",
        "class": "GorillaAdapter",
        "model": "gorilla-openfunctions-v2",
        "suportsFunctionCalls": False
    },
    "Qwen2.5-7B-Instruct": {
        "filePath": "base.llm.qwen_adapter",
        "class": "QwenAdapter",
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "suportsFunctionCalls": True
    },
    "HuggingFace-Llama-3.1-8B-Instruct": {
        "filePath": "base.llm.hugging_face_llama_adapter",
        "class": "HuggingFaceLlamaAdapter",
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "suportsFunctionCalls": False
    }
}