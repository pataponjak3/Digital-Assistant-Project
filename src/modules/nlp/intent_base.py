from abc import ABC, abstractmethod
from typing import Optional, Dict

class IntentRecognizer(ABC):
    @abstractmethod
    def recognize_intent(self, text: str) -> Optional[Dict[str, str]]:
        """
        Returns an intent dictionary like:
        {"intent": "launch_app", "value": "notepad"}
        or None if no match is found.
        """
        pass