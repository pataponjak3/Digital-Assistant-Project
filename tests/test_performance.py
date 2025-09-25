import time

from modules.base.llm.awan_llama_adapter import AwanLlamaAdapter
from modules.base.llm.gemini_adapter import GeminiAdapter
from modules.base.llm.qwen_adapter import QwenAdapter
from modules.base.llm.hugging_face_llama_adapter import HuggingFaceLlamaAdapter
import logging

logger = logging.getLogger(__name__)

def test_weather_execution_time(weather_module):
    args_list = [
        {"lat": 40.7128, "lon": -74.0060},
        {"lat": -33.8688, "lon": 151.2093},
        {"lat": -23.5505, "lon": -46.6333},
        {"lat": 30.0444, "lon": 31.2357},
        {"lat": 55.7558, "lon": 37.6173},
        {"lat": -1.2921, "lon": 36.8219},
        {"lat": 64.1466, "lon": -21.9426},
        {"lat": -33.9249, "lon": 18.4241},
        {"lat": 35.6895, "lon": 139.6917},
        {"lat": 38.7223, "lon": -9.1393},
        {"zip": 10001, "country_code": "US"},
        {"zip": 90210, "country_code": "US"},
        {"zip": 60614, "country_code": "US"},
        {"zip": 10115, "country_code": "DE"},
        {"zip": "SW1A 1AA", "country_code": "GB"},
        {"zip": 75001, "country_code": "FR"},
        {"zip": "1250-096", "country_code": "PT"},
        {"zip": 2000, "country_code": "AU"},
        {"zip": "01000-000", "country_code": "BR"},
        {"zip": 110001, "country_code": "IN"},
        {"city": "Kyoto", "country_code": "JP"},
        {"city": "Toronto", "country_code": "CA"},
        {"city": "Nairobi"},
        {"city": "Auckland", "country_code": "NZ"},
        {"city": "Reykjavik", "country_code": "IS"},
        {"city": "Lima", "country_code": "PE"},
        {"city": "Johannesburg", "country_code": "ZA"},
        {"city": "Munich", "country_code": "DE"},
        {"city": "San Francisco", "state_code": "CA", "country_code": "US"},
        {"city": "Porto", "country_code": "PT"}
    ]
    for args in args_list:
        start = time.perf_counter()
        result = weather_module.execute_function("get_current_weather", args, supports_function_calls=True)
        elapsed = time.perf_counter() - start
        logger.debug(f"get_current_weather, no formatting, with args {args} took {elapsed:.2f}s, with result: \n{result}\n\n")
        assert result is not None
        assert elapsed < 3.0
        start = time.perf_counter()
        result = weather_module.execute_function("get_current_weather", args, supports_function_calls=False)
        elapsed = time.perf_counter() - start
        logger.debug(f"get_current_weather, formatting, with args {args} took {elapsed:.2f}s, with result: \n{result}\n\n")
        assert result is not None
        assert elapsed < 3.0
        start = time.perf_counter()
        result = weather_module.execute_function("get_forecast", args, supports_function_calls=True)
        elapsed = time.perf_counter() - start
        logger.debug(f"get_forecast, no formatting, with args {args} took {elapsed:.2f}s, with result: \n{result}\n\n")
        assert result is not None
        assert elapsed < 3.0
        start = time.perf_counter()
        result = weather_module.execute_function("get_forecast", args, supports_function_calls=False)
        elapsed = time.perf_counter() - start
        logger.debug(f"get_forecast, formatting, with args {args} took {elapsed:.2f}s, with result: \n{result}\n\n")
        assert result is not None
        assert elapsed < 3.0
        start = time.perf_counter()
        result = weather_module.execute_function("get_air_pollution", args, supports_function_calls=True)
        elapsed = time.perf_counter() - start
        logger.debug(f"get_air_pollution, no formatting, with args {args} took {elapsed:.2f}s, with result: \n{result}\n\n")
        assert result is not None
        assert elapsed < 3.0
        start = time.perf_counter()
        result = weather_module.execute_function("get_air_pollution", args, supports_function_calls=False)
        elapsed = time.perf_counter() - start
        logger.debug(f"get_air_pollution, formatting, with args {args} took {elapsed:.2f}s, with result: \n{result}\n\n")
        assert result is not None
        assert elapsed < 3.0
    


def test_os_launch_time(os_module):
    args_list = [
        {"app_name": "Steam"},
        {"app_name": "dis cord"},
        {"app_name": "Eclipse IDE"},
        {"app_name": "VS Code"},
        {"app_name": "visual studio code"},
        {"app_name": "VSC"},
        {"app_name": "Win RAR"},
        {"app_name": "WinRAR"},
        {"app_name": "Google Chorme"},
        {"app_name": "chrome browser"},
        {"app_name": "Firefox"},
        {"app_name": "Notepad"},
        {"app_name": "calc"},
        {"app_name": "VLC"},
        {"app_name": "Spotify"},
        {"app_name": "Adobe Reader"},
        {"app_name": "Acrobat"},
        {"app_name": "Slack"},
        {"app_name": "MS Teams"},
        {"app_name": "Outlok"},
        {"app_name": "Word"},
        {"app_name": "Excel"},
        {"app_name": "Power Point"},
        {"app_name": "Paint"},
        {"app_name": "Edge browser"},
        {"app_name": "Git Extensions"},
        {"app_name": "7Zip"},
        {"app_name": "IntelliJ"},
        {"app_name": "Pychram"},
        {"app_name": "Android Studio"},
    ]
    for args in args_list:
        start = time.perf_counter()
        result = os_module.execute_function("launch_application", args, supports_function_calls=False)
        elapsed = time.perf_counter() - start
        logger.debug(f"launch_application, with args {args} took {elapsed:.2f}s, with result: \n{result}\n\n")
        assert result is not None
        assert elapsed < 2.0

def test_awan_response_normal(new_awan_adapter, conversation_normal):
    llm: AwanLlamaAdapter = new_awan_adapter
    
    for conversation in conversation_normal:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Normal conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_awan_response_current_weather(new_awan_adapter, conversation_current_weather):
    llm: AwanLlamaAdapter = new_awan_adapter
    for conversation in conversation_current_weather:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current weather conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_awan_response_5day_forecast(new_awan_adapter, conversation_5day_forecast):
    llm: AwanLlamaAdapter = new_awan_adapter
    for conversation in conversation_5day_forecast:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"5 day forecast conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)


def test_awan_response_air_pollution(new_awan_adapter, conversation_air_pollution):
    llm: AwanLlamaAdapter = new_awan_adapter
    for conversation in conversation_air_pollution:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current air pollution conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)


def test_awan_response_launch_app(new_awan_adapter, conversation_launch_app):
    llm: AwanLlamaAdapter = new_awan_adapter
    for conversation in conversation_launch_app:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Launch application conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)

def test_gemini_response_normal(new_gemini_adapter, conversation_normal):
    llm: GeminiAdapter = new_gemini_adapter
    for conversation in conversation_normal:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Normal conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_gemini_response_current_weather(new_gemini_adapter, conversation_current_weather):
    llm: GeminiAdapter = new_gemini_adapter
    for conversation in conversation_current_weather:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current weather conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_gemini_response_5day_forecast(new_gemini_adapter, conversation_5day_forecast):
    llm: GeminiAdapter = new_gemini_adapter
    for conversation in conversation_5day_forecast:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"5 day forecast conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)


def test_gemini_response_air_pollution(new_gemini_adapter, conversation_air_pollution):
    llm: GeminiAdapter = new_gemini_adapter
    for conversation in conversation_air_pollution:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current air pollution conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)


def test_gemini_response_launch_app(new_gemini_adapter, conversation_launch_app):
    llm: GeminiAdapter = new_gemini_adapter
    for conversation in conversation_launch_app:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Launch application conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)

def test_qwen_response_normal(new_qwen_adapter, conversation_normal):
    llm: QwenAdapter = new_qwen_adapter
    for conversation in conversation_normal:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Normal conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_qwen_response_current_weather(new_qwen_adapter, conversation_current_weather):
    llm: QwenAdapter = new_qwen_adapter
    for conversation in conversation_current_weather:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current weather conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_qwen_response_5day_forecast(new_qwen_adapter, conversation_5day_forecast):
    llm: QwenAdapter = new_qwen_adapter
    for conversation in conversation_5day_forecast:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"5 day forecast conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)


def test_qwen_response_air_pollution(new_qwen_adapter, conversation_air_pollution):
    llm: QwenAdapter = new_qwen_adapter
    for conversation in conversation_air_pollution:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current air pollution conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)


def test_qwen_response_launch_app(new_qwen_adapter, conversation_launch_app):
    llm: QwenAdapter = new_qwen_adapter
    for conversation in conversation_launch_app:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Launch application conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)

def test_qwen_func_response_normal(new_qwen_func_adapter, conversation_normal):
    llm: QwenAdapter = new_qwen_func_adapter
    for conversation in conversation_normal:
        start = time.time()
        response = llm.chat(conversation, supports_function_calls=True)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Normal conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_qwen_func_response_current_weather(new_qwen_func_adapter, conversation_current_weather):
    llm: QwenAdapter = new_qwen_func_adapter
    for conversation in conversation_current_weather:
        start = time.time()
        response = llm.chat(conversation, supports_function_calls=True)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current weather conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_qwen_func_response_5day_forecast(new_qwen_func_adapter, conversation_5day_forecast):
    llm: QwenAdapter = new_qwen_func_adapter
    for conversation in conversation_5day_forecast:
        start = time.time()
        response = llm.chat(conversation, supports_function_calls=True)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"5 day forecast conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)


def test_qwen_func_response_air_pollution(new_qwen_func_adapter, conversation_air_pollution):
    llm: QwenAdapter = new_qwen_func_adapter
    for conversation in conversation_air_pollution:
        start = time.time()
        response = llm.chat(conversation, supports_function_calls=True)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current air pollution conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)


def test_qwen_func_response_launch_app(new_qwen_func_adapter, conversation_launch_app):
    llm: QwenAdapter = new_qwen_func_adapter
    for conversation in conversation_launch_app:
        start = time.time()
        response = llm.chat(conversation, supports_function_calls=True)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Launch application conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)

def test_hf_llama_response_normal(new_huggingface_llama_adapter, conversation_normal):
    llm: HuggingFaceLlamaAdapter = new_huggingface_llama_adapter
    for conversation in conversation_normal:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Normal conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_hf_llama_response_current_weather(new_huggingface_llama_adapter, conversation_current_weather):
    llm: HuggingFaceLlamaAdapter = new_huggingface_llama_adapter
    for conversation in conversation_current_weather:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current weather conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)

def test_hf_llama_response_5day_forecast(new_huggingface_llama_adapter, conversation_5day_forecast):
    llm: HuggingFaceLlamaAdapter = new_huggingface_llama_adapter
    for conversation in conversation_5day_forecast:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"5 day forecast conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        assert response is not None
        time.sleep(5)


def test_hf_llama_response_air_pollution(new_huggingface_llama_adapter, conversation_air_pollution):
    llm: HuggingFaceLlamaAdapter = new_huggingface_llama_adapter
    for conversation in conversation_air_pollution:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Current air pollution conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)


def test_hf_llama_response_launch_app(new_huggingface_llama_adapter, conversation_launch_app):
    llm: HuggingFaceLlamaAdapter = new_huggingface_llama_adapter
    for conversation in conversation_launch_app:
        start = time.time()
        response = llm.chat(conversation)
        elapsed = time.time() - start
        llm.clear_chat_history()

        logger.debug(f"Launch application conversation '{conversation}' took {elapsed:.2f}s with response: \n{response}\n\n")

        print(f"\nQuery='{conversation}' took {elapsed:.2f}s | response={response}")

        # Example checks
        assert response is not None
        time.sleep(5)
