from abc import ABC, abstractmethod

class RESTServiceInterface(ABC):
    """Interface for REST services."""

    @property
    @abstractmethod
    def _base_url(self) -> str:
        """Base URL for the REST service."""
        pass

    #@__base_url.setter
    #@abstractmethod
    #def __base_url(self, value: str):
    #    """Set the base URL for the REST service."""
    #    pass

    @property
    @abstractmethod
    def _api_key(self) -> str:
        """API key for the REST service."""
        pass

    #@__api_key.setter
    #@abstractmethod
    #def __api_key(self, value: str):
    #    """Set the API key for the REST service."""
    #    pass

    @abstractmethod
    def _send_resquest(self, endpoint: str, params: dict) -> dict:
        """
        Send a request to the REST service.

        :param endpoint: The API endpoint to send the request to.
        :param params: The parameters to include in the request.
        :return: The response from the REST service.
        """
        pass