from abc import ABC, abstractmethod

class RESTService(ABC):
    """Interface for REST services."""

    @property
    @abstractmethod
    def _base_url(self) -> str:
        """
        Base URL for the REST service.
        
        :return: The base URL.
        :rtype: str
        """
        pass

    #@__base_url.setter
    #@abstractmethod
    #def __base_url(self, value: str):
    #    """Set the base URL for the REST service."""
    #    pass

    @property
    @abstractmethod
    def _api_key(self) -> str:
        """
        API key for the REST service.

        :return: The API key.
        :rtype: str
        """
        pass

    #@__api_key.setter
    #@abstractmethod
    #def __api_key(self, value: str):
    #    """Set the API key for the REST service."""
    #    pass

    @abstractmethod
    def _send_resquest(self, method:str, endpoint: str, **kwargs) -> dict:
        """
        Send a request to the REST service.

        :param method: HTTP method (GET, POST, etc.).
        :type method: str
        :param endpoint: The API endpoint to send the request to.
        :type endpoint: str
        :param kwargs: Additional parameters for the request.
        :return: The response from the REST service.
        :rtype: dict
        """
        pass