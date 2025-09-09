import time

from ..src.modules.base.llm.awan_llama_adapter import AwanLlamaAdapter
from ..src.modules.fn.met.meteorology import MeteorologyFunctionality
from ..src.modules.fn.os.os import OSFunctionality
from ..src.utils.function_handler import AssistantFunctionHandler
from ..src.core.assistant_backend import AssistantBackend


def test_awan_response_time(new_awan_adapter_factory, query):
    llm: AwanLlamaAdapter = new_awan_adapter_factory()

    start = time.time()
    response = llm.chat(query, is_not_da_response=True, supports_function_calls=False)
    elapsed = time.time() - start

    print(f"\nQuery='{query}' took {elapsed:.2f}s | response={response}")

    # Example checks
    assert response is not None
    assert elapsed < 10.0


def test_weather_execution_time(weather_module):
    args = {"city": "Lisbon", "units": "metric", "lang": "en"}
    start = time.perf_counter()
    result = weather_module.execute_function("get_current_weather", args, supports_function_calls=False)
    elapsed = time.perf_counter() - start
    assert result is not None
    assert elapsed < 3.0


def test_os_launch_time(os_module):
    args = {"app_name": "notepad"}
    start = time.perf_counter()
    result = os_module.execute_function("launch_application", args, supports_function_calls=False)
    elapsed = time.perf_counter() - start
    assert result is not None
    assert elapsed < 2.0