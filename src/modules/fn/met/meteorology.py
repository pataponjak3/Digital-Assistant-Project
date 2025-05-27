from ....interfaces.rest_service import RESTServiceInterface
from ....interfaces.functionality import DAFunctionalityInterface
import requests

class MeteorologyService(RESTServiceInterface, DAFunctionalityInterface):
    def __init__(self, api_key:str):
        self.__base_url = "api.openweathermap.org"
        self.__geo_url = self.__base_url + "/geo/1.0"
        self.__data_url = self.__base_url + "/data/2.5"
        self.__api_key = api_key

    def __send_resquest(self, url: str, params: dict) -> dict:
        """Send a request to the REST service."""
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_functions_schemas(self) -> list[dict]:
        return [
            {
                "name": "get_current_weather",
                "description": "Retrieve the current weather for a location.",
                "response_format": ["json"],
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lat": {"type": "number", "description": "Latitude (-90 to 90)."},
                        "lon": {"type": "number", "description": "Longitude (-180 to 180)."},
                        "city": {"type": "string", "description": "City name."},
                        "state_code": {"type": "string", "description": "State code (US only)."},
                        "country_code": {"type": "string", "description": "ISO 3166 country code."},
                        "zip": {"type": "string", "description": "Postal code."},
                        "units": {"type": "string", "description": "Temperature unit: kelvin (default), celsius, fahrenheit."},
                        "lang": {"type": "string", "description": "Language code for weather description (e.g., 'en')."}
                    },
                    "description": "Provide either (1) 'lat' and 'lon', or (2) 'zip' and 'country_code', or (3) 'city' (optionally with 'state_code' and 'country_code')."

                },
                "response_schema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "coord": {
                                "type": "object",
                                "properties": {
                                    "lon": {"type": "number", "description": "Longitude of the location."},
                                    "lat": {"type": "number", "description": "Latitude of the location."}
                                }
                            },
                            "weather": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {"type": "number", "description": "Weather condition id."},
                                        "main": {"type": "string", "description": "Group of weather parameters (Rain, Snow, Clouds etc.)."},
                                        "description": {"type": "string", "description": "Weather condition within the group."},
                                        "icon": {"type": "string", "description": "Weather icon id."}
                                    }
                                }
                            },
                            "base": {"type": "string", "description": "Internal parameter."},
                            "main": {
                                "type": "object",
                                "properties": {
                                    "temp": {"type": "number", "description": "Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
                                    "feels_like": {"type": "number", "description": "Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
                                    "pressure": {"type": "number", "description": "Atmospheric pressure on the sea level, hPa."},
                                    "humidity": {"type": "number", "description": "Humidity, %."},
                                    "temp_min": {"type": "number", "description": "Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
                                    "temp_max": {"type": "number", "description": "Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
                                    "sea_level": {"type": "number", "description": "Atmospheric pressure on the sea level, hPa."},
                                    "grnd_level": {"type": "number", "description": "Atmospheric pressure on the ground level, hPa"}
                                }
                            },
                            "visibility": {"type": "number", "description": "Visibility, meter. The maximum value of the visibility is 10 km."},
                            "wind": {
                                "type": "object",
                                "properties": {
                                    "speed": {"type": "number", "description": "Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour."},
                                    "deg": {"type": "number", "description": "Wind direction, degrees (meteorological)."},
                                    "gust": {"type": "number", "description": "Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour."}
                                }
                            },
                            "clouds": {
                                "type": "object",
                                "properties": {
                                    "all": {"type": "number", "description": "Cloudiness, %."}
                                }
                            },
                            "rain": {
                                "type": "object",
                                "properties": {
                                    "1h": {"type": "number", "description": "(where available) Precipitation, mm/h. Please note that only mm/h as units of measurement are available for this parameter."},
                                }
                            },
                            "snow":{
                                "type": "object",
                                "properties": {
                                    "1h": {"type": "number", "description": "(where available) Precipitation, mm/h. Please note that only mm/h as units of measurement are available for this parameter."}
                                }
                            },
                            "dt": {"type": "number", "description": "Time of data calculation, unix, UTC."},
                            "sys": {
                                "type": "object",
                                "properties": {
                                    "type": {"type": "number", "description": "Internal parameter."},
                                    "id": {"type": "number", "description": "Internal parameter."},
                                    "message": {"type": "string", "description": "Internal parameter."},
                                    "country": {"type": "string", "description": "Country code (GB, JP etc.)."},
                                    "sunrise": {"type": "number", "description": "Sunrise time, unix, UTC."},
                                    "sunset": {"type": "number", "description": "Sunset time, unix, UTC."}
                                }
                            },
                            "timezone": {"type": "number", "description": "Shift in seconds from UTC."},
                            "id": {"type": "number", "description": "City ID."},
                            "name": {"type": "string", "description": "City name."},
                            "cod": {"type": "number", "description": "Internal parameter."}
                        }
                    }
                }
            },
            {
                "name": "get_forecast",
                "description": "Get a 5-day weather forecast in 3-hour intervals.",
                "response_format": ["json"],
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lat": {"type": "number", "description": "Latitude (-90 to 90)."},
                        "lon": {"type": "number", "description": "Longitude (-180 to 180)."},
                        "city": {"type": "string", "description": "City name."},
                        "state_code": {"type": "string", "description": "State code (US only)."},
                        "country_code": {"type": "string", "description": "ISO 3166 country code."},
                        "zip": {"type": "string", "description": "Postal code."},
                        "units": {"type": "string", "description": "Temperature unit: kelvin (default), celsius, fahrenheit."},
                        "lang": {"type": "string", "description": "Language code for weather description (e.g., 'en')."}
                    },
                    "description": "Provide either (1) 'lat' and 'lon', or (2) 'zip' and 'country_code', or (3) 'city' (optionally with 'state_code' and 'country_code')."
                },
                "response_schema":{
                    "json":{
                        "type": "object",
                        "properties": {
                            "cod": {"type": "string", "description": "Internal parameter."},
                            "message": {"type": "number", "description": "Internal parameter."},
                            "cnt": {"type": "number", "description": "A number of timestamps returned in the API response."},
                            "list": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "dt": {"type": "number", "description": "Time of data forecasted, unix, UTC."},
                                        "main": {
                                            "type": "object",
                                            "properties": {
                                                "temp": {"type": "number", "description": "Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
                                                "feels_like": {"type": "number", "description": "This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
                                                "temp_min": {"type": "number", "description": "Minimum temperature at the moment of calculation. This is minimal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
                                                "temp_max": {"type": "number", "description": "Maximum temperature at the moment of calculation. This is maximal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
                                                "pressure": {"type": "number", "description": "Atmospheric pressure on the sea level by default, hPa."},
                                                "sea_level": {"type": "number", "description": "Atmospheric pressure on the sea level, hPa."},
                                                "grnd_level": {"type": "number", "description": "Atmospheric pressure on the ground level, hPa."},
                                                "humidity": {"type": "number", "description": "Humidity, %."},
                                                "temp_kf": {"type": "number", "description": "Internal parameter."}
                                            }
                                        },
                                        "weather":{
                                            "type": "object",
                                            "properties": {
                                                "id": {"type": "number", "description": "Weather condition id."},
                                                "main": {"type": "string", "description": "Group of weather parameters (Rain, Snow, Clouds etc.)."},
                                                "description": {"type": "string", "description": "Weather condition within the group."},
                                                "icon": {"type": "string", "description": "Weather icon id."}
                                            }
                                        },
                                        "clouds":{
                                            "type": "object",
                                            "properties": {
                                                "all": {"type": "number", "description": "Cloudiness, %."}
                                            }
                                        },
                                        "wind":{
                                            "type": "object",
                                            "properties": {
                                                "speed": {"type": "number", "description": "Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour."},
                                                "deg": {"type": "number", "description": "Wind direction, degrees (meteorological)."},
                                                "gust": {"type": "number", "description": "Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour."}
                                            }
                                        },
                                        "visibility": {"type": "number", "description": "Average visibility, metres. The maximum value of the visibility is 10km."},
                                        "pop": {"type": "number", "description": "Probability of precipitation. The values of the parameter vary between 0 and 1, where 0 is equal to 0%, 1 is equal to 100%."},
                                        "rain": {
                                            "type": "object",
                                            "properties": {
                                                "3h": {"type": "number", "description": "Rain volume for last 3 hours, mm. Please note that only mm as units of measurement are available for this parameter."}
                                            }
                                        },
                                        "snow": {
                                            "type": "object",
                                            "properties": {
                                                "3h": {"type": "number", "description": "Snow volume for last 3 hours. Please note that only mm as units of measurement are available for this parameter."}
                                            }
                                        },
                                        "sys":{
                                            "type": "object",
                                            "properties": {
                                                "pod": {"type": "string", "description": "Part of the day (n - night, d - day)."}
                                            }
                                        },
                                        "dt_txt": {"type": "string", "description": "Time of data forecasted, ISO, UTC."}
                                    }
                                }
                            },
                            "city": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "number", "description": "City ID."},
                                    "name": {"type": "string", "description": "City name."},
                                    "coord": {
                                        "type": "object",
                                        "properties": {
                                            "lat": {"type": "number", "description": "Geo location, latitude."},
                                            "lon": {"type": "number", "description": "Geo location, longitude."}
                                        }
                                    },
                                    "country": {"type": "string", "description": "Country code (GB, JP etc.)."},
                                    "population": {"type": "number", "description": "City population"},
                                    "timezone": {"type": "number", "description": "Shift in seconds from UTC."},
                                    "sunrise": {"type": "number", "description": "Sunrise time, Unix, UTC."},
                                    "sunset": {"type": "number", "description": "Sunset time, Unix, UTC."}
                                }
                            }
                        }
                    }
                }
            },
            {
                "name": "get_air_pollution",
                "description": "Get air pollution index and pollutant levels for a location, at the current moment.",
                "response_format": ["json"],
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lat": {"type": "number", "description": "Latitude (-90 to 90)."},
                        "lon": {"type": "number", "description": "Longitude (-180 to 180)."},
                        "city": {"type": "string", "description": "City name."},
                        "state_code": {"type": "string", "description": "State code (US only)."},
                        "country_code": {"type": "string", "description": "ISO 3166 country code."},
                        "zip": {"type": "string", "description": "Postal code."},
                        "units": {"type": "string", "description": "Temperature unit: kelvin (default), celsius, fahrenheit."},
                        "lang": {"type": "string", "description": "Language code for weather description (e.g., 'en')."}
                    },
                    "description": "Provide either (1) 'lat' and 'lon', or (2) 'zip' and 'country_code', or (3) 'city' (optionally with 'state_code' and 'country_code')."
                },
                "response_schema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "coord": {
                                "type": "array",
                                "items": {
                                    "type": "number"
                                },
                                "description": "Coordinates from the specified location (latitude, longitude)."
                            },
                            "list": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "dt": {"type": "number", "description": "Date and time, Unix, UTC."},
                                        "main": {
                                            "type": "object",
                                            "properties": {
                                                "aqi": {"type": "number", "description": " Air Quality Index. Possible values: 1, 2, 3, 4, 5. Where 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor."}
                                            }
                                        },
                                        "components": {
                                            "type": "object",
                                            "properties": {
                                                "co": {"type": "number", "description": "Concentration of CO (Carbon monoxide), μg/m3."},
                                                "no": {"type": "number", "description": "Concentration of NO (Nitrogen monoxide), μg/m3."},
                                                "no2": {"type": "number", "description": "Concentration of NO2 (Nitrogen dioxide), μg/m3."},
                                                "o3": {"type": "number", "description": " Concentration of O3 (Ozone), μg/m3."},
                                                "so2": {"type": "number", "description": "Concentration of SO2 (Sulphur dioxide), μg/m3."},
                                                "pm2_5": {"type": "number", "description": "Concentration of PM2.5 (Fine particles matter), μg/m3."},
                                                "pm10": {"type": "number", "description": "Concentration of PM10 (Coarse particulate matter), μg/m3."},
                                                "nh3": {"type": "number", "description": "Concentration of NH3 (Ammonia), μg/m3."}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        ]

    def execute_function(self, name: str, args: dict):
        return getattr(self, f"__{name}")(**args)
    
    def __resolve_coordinates(self, **kwargs) -> tuple[float, float]:
        """Get the geocoding information for a given location if not provided directly."""
        if "lat" in kwargs and "lon" in kwargs:
            return kwargs["lat"], kwargs["lon"]

        elif "zip" in kwargs and "country_code" in kwargs:
            # Zip geocode lookup
            url = f"{self.__geo_url}/zip"
            params = {
                "zip": f"{kwargs['zip']},{kwargs['country_code']}",
                "appid": self.__api_key
            }
            data = self.__send_resquest(url, params)
            return data["lat"], data["lon"]

        elif "city" in kwargs:
            # Direct geocode lookup
            url = f"{self.__geo_url}/direct"
            q = kwargs["city"]
            if "state_code" in kwargs:
                q += f",{kwargs['state_code']}"
            if "country_code" in kwargs:
                q += f",{kwargs['country_code']}"
            params = {
                "q": q,
                "limit": 1,
                "appid": self.__api_key
            }
            data = self.__send_resquest(url, params)
            if not data:
                raise ValueError("No results found for the given location.")
            return data[0]["lat"], data[0]["lon"]

        else:
            raise ValueError("Insufficient location information. Provide lat/lon, city, or zip + country_code.")
    
    def __get_current_weather(self, **kwargs) -> dict:
        lat, lon = self.__resolve_coordinates(**kwargs)

        url = f"{self.__data_url}/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.__api_key,
            "units": kwargs.get("units", "standard"),
            "lang": kwargs.get("lang", "en")
        }

        return self.__send_resquest(url, params)
    
    def __get_forecast(self, **kwargs) -> dict:
        lat, lon = self.__resolve_coordinates(**kwargs)

        url = f"{self.__data_url}/forecast"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.__api_key,
            "units": kwargs.get("units", "standard"),
            "lang": kwargs.get("lang", "en")
        }

        return self.__send_resquest(url, params)
    
    def __get_air_pollution(self, **kwargs) -> dict:
        lat, lon = self.__resolve_coordinates(**kwargs)

        url = f"{self.__data_url}/air_pollution"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.__api_key
        }

        return self.__send_resquest(url, params)
