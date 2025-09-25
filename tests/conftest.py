import pytest
from modules.base.llm.awan_llama_adapter import AwanLlamaAdapter
from modules.base.llm.gemini_adapter import GeminiAdapter
from modules.base.llm.qwen_adapter import QwenAdapter
from modules.base.llm.hugging_face_llama_adapter import HuggingFaceLlamaAdapter
from utils.function_handler import AssistantFunctionHandler
from utils.system_prompt_generator import AssistantSystemPromptGenerator
from core.assistant_backend import AssistantBackend
from config.config import ModuleLoader

modules = ModuleLoader().load_functionality_modules()
prompt_noFunc = AssistantSystemPromptGenerator(modules).generate(False)
prompt_func = AssistantSystemPromptGenerator(modules).generate(True)
tools = []
for module in modules.values():
    tools.extend(module.get_functions_schema())

@pytest.fixture(scope="session")
def new_awan_llama_adapter():
    return AwanLlamaAdapter("Meta-Llama-3.1-8B-Instruct", prompt_noFunc)

@pytest.fixture(scope="session")
def new_gemini_adapter():
    return GeminiAdapter("gemini-2.0-flash", prompt_noFunc)

@pytest.fixture(scope="session")
def new_qwen_adapter():
    return QwenAdapter("Qwen/Qwen2.5-7B-Instruct", prompt_noFunc)

@pytest.fixture(scope="session")
def new_qwen_func_adapter():
    return QwenAdapter("Qwen/Qwen2.5-7B-Instruct", prompt_func, tools)

@pytest.fixture(scope="session")
def new_huggingface_llama_adapter():
    return HuggingFaceLlamaAdapter("meta-llama/Llama-3.1-8B-Instruct", prompt_noFunc)

@pytest.fixture(scope="session")
def weather_module():
    return modules.get("meteorology")

@pytest.fixture(scope="session")
def os_module():
    return modules.get("os")

@pytest.fixture(scope="session")
def function_handler():
    return AssistantFunctionHandler(modules)

@pytest.fixture(scope="session")
def backend(llm_adapter, function_handler):
    # Construct your backend with the LLM and modules
    return AssistantBackend(
        llm_adapter=llm_adapter,
        function_handler=function_handler,
        llm_supports_function_calls=False
    )

@pytest.fixture(scope="session")
def conversation_normal():
    return [
        "Explain the difference between threads and processes in one paragraph.",
        "Give me 3 meal prep ideas for a vegetarian who trains for half-marathons.",
        "Summarize the key idea of 'inversion' from mental models (keep it short).",
        "What are common pitfalls when using Python's asyncio with CPU-bound work?",
        "Draft a friendly email asking for a project deadline extension.",
        "What's a good daily warm-up routine for desk workers? Keep it under 8 steps.",
        "I keep forgetting people's names—share 4 memory techniques.",
        "Turn this into a bullet list: 'Plan, execute, measure, iterate.' Add one emoji each.",
        "Write a tiny story (≤120 words) about a lighthouse learning Morse code.",
        "Explain CAP theorem like I'm new to distributed systems.",
        "Compare SQLite vs PostgreSQL for a solo desktop app.",
        "How would you unit test a function that parses CSV lines? Keep it high level.",
        "What's the minimum I need to know about UX heuristics to not mess up my UI?",
        "I'm anxious before presentations—give me 5 quick tips.",
        "Rewrite 'optimize the pipeline' in plainer language.",
        "Brainstorm 6 team-building activities for remote developers.",
        "What's the trade-off between early abstraction and duplication?",
        "Explain why floating-point math can be surprising to newcomers.",
        "Give me a one-liner pep talk for debugging at 2 a.m.",
        "List 5 git hygiene practices for small teams.",
        "What's a simple analogy for gradient descent?",
        "Suggest 4 interview questions to test problem decomposition skills.",
        "How do I politely push back on scope creep?",
        "Convert this to title case: 'an introduction to concurrency primitives'",
        "Name 5 signs a backlog item isn't ready for dev.",
        "What's a good rubric to decide whether to refactor now or later?",
        "Give me a tiny regex cheat sheet (anchors, groups, classes).",
        "What's the 80/20 of Docker I should know to ship a Python app?",
        "Explain the difference between correlation and causation with one example.",
        "Turn 'I will try' into 3 stronger alternatives."
    ]

@pytest.fixture(scope="session")
def conversation_current_weather():
    return[
        "Current weather at 40.7128, -74.0060?",
        "What's it like now near -33.8688, 151.2093 (Sydny)?",
        "Weather rn at -23.5505, -46.6333.",
        "Temp & conditions at 30.0444, 31.2357 please.",
        "What's the current weather @ 55.7558, 37.6173?",
        "Is it raining around -1.2921, 36.8219 right now?",
        "How cold is it near 64.1466, -21.9426?",
        "Current wind & temp for -33.9249, 18.4241.",
        "Weather now at 35.6895, 139.6917 (Tokio)?",
        "What's the weather like at 38.7223, -9.1393?",
        "Current weather for zip 10001, US.",
        "Weather now at 90210, US?",
        "How's Chicago right now—60614, US.",
        "What's it like at 10115, DE (Berlin)?",
        "Weather for SW1A 1AA, GB (Buckingham)?",
        "Now in 75001, FR?",
        "Current weather for 1250-096, PT (Lisboa)?",
        "What's it now at 2000, AU (Sydney CBD)?",
        "Weather rn at 01000-000, BR (São Paulo).",
        "Current conditions for 110001, IN (New Delhi).",
        "What's the weather in Kyoto, JP right now?",
        "Current conditions in Toronto, CA?",
        "How's Nairobi today?",
        "Weather now in Auckland, NZ.",
        "What's it like in Reykyavik, IS?",
        "Current weather for Lima, PE.",
        "How's Jo'burg (Johannesburg, ZA) right now?",
        "Weather in Munich, DE (now).",
        "Current conditions San Francisco, US-CA.",
        "What's the weather in Porto, PT?"
    ]

@pytest.fixture(scope="session")
def conversation_5day_forecast():
    return [
        "5-day forecast for 40.7128, -74.0060.",
        "Next 5 days near -33.8688, 151.2093?",
        "Forecast (5d) at -23.5505, -46.6333.",
        "Show me 5-day outlook for 30.0444, 31.2357.",
        "What's the week ahead at 55.7558, 37.6173?",
        "Five-day forecast around -1.2921, 36.8219.",
        "Is it cooling later this week near 64.1466, -21.9426?",
        "Give 5-day hi/lo for -33.9249, 18.4241.",
        "Forecast next days at 35.6895, 139.6917.",
        "Five-day for 38.7223, -9.1393 (Lisbon).",
        "5-day forecast 10001, US.",
        "Forecast for 90210, US next 5 days.",
        "Weather outlook 60614, US.",
        "5-day for 10115, DE.",
        "Next five days SW1A 1AA, GB.",
        "Forecast 75001, FR.",
        "5-day for 1250-096, PT.",
        "Forecast for 2000, AU.",
        "5-day outlook 01000-000, BR.",
        "Next 5 days 110001, IN.",
        "Five-day forecast Kyoto, JP.",
        "What's the 5-day in Toronto, CA?",
        "5-day forecast Nairobi.",
        "Week ahead in Auckland, NZ.",
        "5-day for Reykjavik, IS (typo earlier).",
        "Forecast 5 days Lima, PE.",
        "Next 5 days Johannesburg, ZA.",
        "Munich, DE 5-day outlook.",
        "San Francisco, US-CA 5-day forecast.",
        "5-day for Porto, PT."
    ]

@pytest.fixture(scope="session")
def conversation_air_pollution():
    return [
        "Current air quality at 40.7128, -74.0060?",
        "AQI near -33.8688, 151.2093 right now.",
        "What's PM2.5 at -23.5505, -46.6333?",
        "Air pollution for 30.0444, 31.2357.",
        "AQI around 55.7558, 37.6173 (Moscow).",
        "Current AQI for -1.2921, 36.8219.",
        "Is air clean near 64.1466, -21.9426?",
        "Pollution stats at -33.9249, 18.4241.",
        "AQI now 35.6895, 139.6917.",
        "Air quality 38.7223, -9.1393.",
        "Air quality for 10001, US.",
        "AQI now at 90210, US.",
        "Pollution level 60614, US.",
        "AQI 10115, DE.",
        "Air quality SW1A 1AA, GB.",
        "AQI 75001, FR.",
        "Air quality 1250-096, PT.",
        "AQI 2000, AU.",
        "Air quality 01000-000, BR.",
        "AQI 110001, IN.",
        "Current AQI Kyoto, JP.",
        "Air quality Toronto, CA now.",
        "AQI Nairobi?",
        "Air quality in Auckland, NZ.",
        "AQI Reykjavik, IS (sorry for prev typo).",
        "Pollution level Lima, PE.",
        "AQI Johannesburg, ZA.",
        "Air quality Munich, DE.",
        "AQI San Francisco, US-CA.",
        "Air quality Porto, PT."
    ]

@pytest.fixture(scope="session")
def conversation_launch_app():
    return [
        "Open Steam.",
        "Launch dis cord.",
        "Start Eclipse IDE.",
        "Open VS Code.",
        "Run visual studio code pls.",
        "Launch VSC.",
        "Open Win RAR.",
        "Start WinRAR.",
        "Open Google Chorme.",
        "Launch chrome browser.",
        "Open Firefox.",
        "Start Notepad.",
        "Launch calc.",
        "Open VLC.",
        "Start Spotify.",
        "Open Adobe Reader.",
        "Launch Acrobat.",
        "Open Slack.",
        "Start MS Teams.",
        "Open Outlok.",
        "Launch Word.",
        "Open Excel.",
        "Start Power Point.",
        "Open Paint.",
        "Start Edge browser.",
        "Launch Git Extensions.",
        "Open 7Zip.",
        "Start IntelliJ.",
        "Open Pychram.",
        "Launch Android Studio.",
    ]