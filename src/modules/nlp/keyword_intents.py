from .intent_base import IntentRecognizer
from typing import Optional, Dict

class KeywordIntentRecognizer(IntentRecognizer):
    def __init__(self):
        # Define simple intents and their associated keywords
        self.intent_keywords = {
            "launch_app": ["open notepad", "launch calculator", "start browser"],
            "get_weather": ["weather", "temperature", "forecast"],
            "exit": ["exit", "quit", "close assistant"]
        }

    def recognize_intent(self, text: str) -> Optional[Dict[str, str]]:
        text = text.lower()
        for intent, keywords in self.intent_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    return {"intent": intent, "value": keyword}
        return None