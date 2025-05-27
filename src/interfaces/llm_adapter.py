from abc import ABC, abstractmethod

class LLMAdapterInterface(ABC):
    @abstractmethod
    def chat(self, messages: list[dict], functions: list[dict] = None) -> dict:
        """
        Send a chat message to the LLM and get a response.
        :param messages: List of message dicts (role, content).
        :param functions: (Optional) Function schemas.
        :return: Dict containing the LLM response.
        """

    @abstractmethod
    def get_provider_name(self) -> str:
        """Return the name of the LLM provider."""