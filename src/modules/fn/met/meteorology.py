from ..rest_service import RESTServiceInterface

class MeteorologyService(RESTServiceInterface):
    def __init__(self, api_key:str):
        self.__base_url = "api.openweathermap.org"
        self.__api_key = api_key
        