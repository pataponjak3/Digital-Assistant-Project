from ....interfaces.rest_service import RESTServiceInterface
from ....interfaces.functionality import DAFunctionalityInterface
from ....core.config import APIKeyManager
import requests, datetime

class MeteorologyService(RESTServiceInterface, DAFunctionalityInterface):
    def __init__(self):
        self.__base_url = "https://api.openweathermap.org"
        self.__geo_url = self.__base_url + "/geo/1.0"
        self.__data_url = self.__base_url + "/data/2.5"
        self.__icons = "https://openweathermap.org/img/wn/"
        self.__api_key = APIKeyManager().get_key("openweathermap")
        self.__units = {"metric": "°C", "imperial": "°F", "standard": "K"}

    def _api_key(self):
        return self.__api_key
    
    def _base_url(self):
        return self.__base_url

    def _send_resquest(self, url: str, params: dict) -> dict:
        """Send a request to the REST service."""
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_functions_description(self) -> list[str]:
        return [
"""Function: get_current_weather
Module: meteorology
Description: Get the current weather for a location.
Arguments:
- city (string): City name. Optionally add state_code (only for USA) and country_code (follows ISO 3166).
- lat (number) and lon (number): Coordinates (-90 to 90, -180 to 180).
- zip (string) and country_code (string): Postal code and country code.
- units (string): Optional. Temperature unit: standart, metric, imperial.
- lang (string): Optional. Language code for weather description (e.g., 'en').""",
"""Function: get_forecast
Module: meteorology
Description: Get a 5-day forecast in 3-hour intervals.
Arguments: Same as get_current_weather.""",
"""Function: get_air_pollution
Module: meteorology
Description: Get current air pollution data for a location.
Arguments: Same as get_current_weather."""
            # {
            #     "name": "get_current_weather",
            #     "module": "meteorology",
            #     "description": "Retrieve the current weather for a location.",
            #     "response_format": ["json"],
            #     "parameters": {
            #         "type": "object",
            #         "properties": {
            #             "lat": {"type": "number", "description": "Latitude (-90 to 90)."},
            #             "lon": {"type": "number", "description": "Longitude (-180 to 180)."},
            #             "city": {"type": "string", "description": "City name."},
            #             "state_code": {"type": "string", "description": "State code (US only)."},
            #             "country_code": {"type": "string", "description": "ISO 3166 country code."},
            #             "zip": {"type": "string", "description": "Postal code."},
            #             "units": {"type": "string", "description": "Temperature unit: kelvin (default), celsius, fahrenheit."},
            #             "lang": {"type": "string", "description": "Language code for weather description (e.g., 'en')."}
            #         },
            #         "description": "Provide either (1) 'lat' and 'lon', or (2) 'zip' and 'country_code', or (3) 'city' (optionally with 'state_code' and 'country_code')."

            #     },
            #     "response_schema": {
            #         "json": {
            #             "type": "object",
            #             "properties": {
            #                 "coord": {
            #                     "type": "object",
            #                     "properties": {
            #                         "lon": {"type": "number", "description": "Longitude of the location."},
            #                         "lat": {"type": "number", "description": "Latitude of the location."}
            #                     }
            #                 },
            #                 "weather": {
            #                     "type": "array",
            #                     "items": {
            #                         "type": "object",
            #                         "properties": {
            #                             "id": {"type": "number", "description": "Weather condition id."},
            #                             "main": {"type": "string", "description": "Group of weather parameters (Rain, Snow, Clouds etc.)."},
            #                             "description": {"type": "string", "description": "Weather condition within the group."},
            #                             "icon": {"type": "string", "description": "Weather icon id."}
            #                         }
            #                     }
            #                 },
            #                 "base": {"type": "string", "description": "Internal parameter."},
            #                 "main": {
            #                     "type": "object",
            #                     "properties": {
            #                         "temp": {"type": "number", "description": "Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
            #                         "feels_like": {"type": "number", "description": "Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
            #                         "pressure": {"type": "number", "description": "Atmospheric pressure on the sea level, hPa."},
            #                         "humidity": {"type": "number", "description": "Humidity, %."},
            #                         "temp_min": {"type": "number", "description": "Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
            #                         "temp_max": {"type": "number", "description": "Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
            #                         "sea_level": {"type": "number", "description": "Atmospheric pressure on the sea level, hPa."},
            #                         "grnd_level": {"type": "number", "description": "Atmospheric pressure on the ground level, hPa"}
            #                     }
            #                 },
            #                 "visibility": {"type": "number", "description": "Visibility, meter. The maximum value of the visibility is 10 km."},
            #                 "wind": {
            #                     "type": "object",
            #                     "properties": {
            #                         "speed": {"type": "number", "description": "Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour."},
            #                         "deg": {"type": "number", "description": "Wind direction, degrees (meteorological)."},
            #                         "gust": {"type": "number", "description": "Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour."}
            #                     }
            #                 },
            #                 "clouds": {
            #                     "type": "object",
            #                     "properties": {
            #                         "all": {"type": "number", "description": "Cloudiness, %."}
            #                     }
            #                 },
            #                 "rain": {
            #                     "type": "object",
            #                     "properties": {
            #                         "1h": {"type": "number", "description": "(where available) Precipitation, mm/h. Please note that only mm/h as units of measurement are available for this parameter."},
            #                     }
            #                 },
            #                 "snow":{
            #                     "type": "object",
            #                     "properties": {
            #                         "1h": {"type": "number", "description": "(where available) Precipitation, mm/h. Please note that only mm/h as units of measurement are available for this parameter."}
            #                     }
            #                 },
            #                 "dt": {"type": "number", "description": "Time of data calculation, unix, UTC."},
            #                 "sys": {
            #                     "type": "object",
            #                     "properties": {
            #                         "type": {"type": "number", "description": "Internal parameter."},
            #                         "id": {"type": "number", "description": "Internal parameter."},
            #                         "message": {"type": "string", "description": "Internal parameter."},
            #                         "country": {"type": "string", "description": "Country code (GB, JP etc.)."},
            #                         "sunrise": {"type": "number", "description": "Sunrise time, unix, UTC."},
            #                         "sunset": {"type": "number", "description": "Sunset time, unix, UTC."}
            #                     }
            #                 },
            #                 "timezone": {"type": "number", "description": "Shift in seconds from UTC."},
            #                 "id": {"type": "number", "description": "City ID."},
            #                 "name": {"type": "string", "description": "City name."},
            #                 "cod": {"type": "number", "description": "Internal parameter."}
            #             }
            #         }
            #     }
            # },
            # {
            #     "name": "get_forecast",
            #     "module": "meteorology",
            #     "description": "Get a 5-day weather forecast in 3-hour intervals.",
            #     "response_format": ["json"],
            #     "parameters": {
            #         "type": "object",
            #         "properties": {
            #             "lat": {"type": "number", "description": "Latitude (-90 to 90)."},
            #             "lon": {"type": "number", "description": "Longitude (-180 to 180)."},
            #             "city": {"type": "string", "description": "City name."},
            #             "state_code": {"type": "string", "description": "State code (US only)."},
            #             "country_code": {"type": "string", "description": "ISO 3166 country code."},
            #             "zip": {"type": "string", "description": "Postal code."},
            #             "units": {"type": "string", "description": "Temperature unit: kelvin (default), celsius, fahrenheit."},
            #             "lang": {"type": "string", "description": "Language code for weather description (e.g., 'en')."}
            #         },
            #         "description": "Provide either (1) 'lat' and 'lon', or (2) 'zip' and 'country_code', or (3) 'city' (optionally with 'state_code' and 'country_code')."
            #     },
            #     "response_schema":{
            #         "json":{
            #             "type": "object",
            #             "properties": {
            #                 "cod": {"type": "string", "description": "Internal parameter."},
            #                 "message": {"type": "number", "description": "Internal parameter."},
            #                 "cnt": {"type": "number", "description": "A number of timestamps returned in the API response."},
            #                 "list": {
            #                     "type": "array",
            #                     "items": {
            #                         "type": "object",
            #                         "properties": {
            #                             "dt": {"type": "number", "description": "Time of data forecasted, unix, UTC."},
            #                             "main": {
            #                                 "type": "object",
            #                                 "properties": {
            #                                     "temp": {"type": "number", "description": "Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
            #                                     "feels_like": {"type": "number", "description": "This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
            #                                     "temp_min": {"type": "number", "description": "Minimum temperature at the moment of calculation. This is minimal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
            #                                     "temp_max": {"type": "number", "description": "Maximum temperature at the moment of calculation. This is maximal forecasted temperature (within large megalopolises and urban areas), use this parameter optionally. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit."},
            #                                     "pressure": {"type": "number", "description": "Atmospheric pressure on the sea level by default, hPa."},
            #                                     "sea_level": {"type": "number", "description": "Atmospheric pressure on the sea level, hPa."},
            #                                     "grnd_level": {"type": "number", "description": "Atmospheric pressure on the ground level, hPa."},
            #                                     "humidity": {"type": "number", "description": "Humidity, %."},
            #                                     "temp_kf": {"type": "number", "description": "Internal parameter."}
            #                                 }
            #                             },
            #                             "weather":{
            #                                 "type": "object",
            #                                 "properties": {
            #                                     "id": {"type": "number", "description": "Weather condition id."},
            #                                     "main": {"type": "string", "description": "Group of weather parameters (Rain, Snow, Clouds etc.)."},
            #                                     "description": {"type": "string", "description": "Weather condition within the group."},
            #                                     "icon": {"type": "string", "description": "Weather icon id."}
            #                                 }
            #                             },
            #                             "clouds":{
            #                                 "type": "object",
            #                                 "properties": {
            #                                     "all": {"type": "number", "description": "Cloudiness, %."}
            #                                 }
            #                             },
            #                             "wind":{
            #                                 "type": "object",
            #                                 "properties": {
            #                                     "speed": {"type": "number", "description": "Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour."},
            #                                     "deg": {"type": "number", "description": "Wind direction, degrees (meteorological)."},
            #                                     "gust": {"type": "number", "description": "Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour."}
            #                                 }
            #                             },
            #                             "visibility": {"type": "number", "description": "Average visibility, metres. The maximum value of the visibility is 10km."},
            #                             "pop": {"type": "number", "description": "Probability of precipitation. The values of the parameter vary between 0 and 1, where 0 is equal to 0%, 1 is equal to 100%."},
            #                             "rain": {
            #                                 "type": "object",
            #                                 "properties": {
            #                                     "3h": {"type": "number", "description": "Rain volume for last 3 hours, mm. Please note that only mm as units of measurement are available for this parameter."}
            #                                 }
            #                             },
            #                             "snow": {
            #                                 "type": "object",
            #                                 "properties": {
            #                                     "3h": {"type": "number", "description": "Snow volume for last 3 hours. Please note that only mm as units of measurement are available for this parameter."}
            #                                 }
            #                             },
            #                             "sys":{
            #                                 "type": "object",
            #                                 "properties": {
            #                                     "pod": {"type": "string", "description": "Part of the day (n - night, d - day)."}
            #                                 }
            #                             },
            #                             "dt_txt": {"type": "string", "description": "Time of data forecasted, ISO, UTC."}
            #                         }
            #                     }
            #                 },
            #                 "city": {
            #                     "type": "object",
            #                     "properties": {
            #                         "id": {"type": "number", "description": "City ID."},
            #                         "name": {"type": "string", "description": "City name."},
            #                         "coord": {
            #                             "type": "object",
            #                             "properties": {
            #                                 "lat": {"type": "number", "description": "Geo location, latitude."},
            #                                 "lon": {"type": "number", "description": "Geo location, longitude."}
            #                             }
            #                         },
            #                         "country": {"type": "string", "description": "Country code (GB, JP etc.)."},
            #                         "population": {"type": "number", "description": "City population"},
            #                         "timezone": {"type": "number", "description": "Shift in seconds from UTC."},
            #                         "sunrise": {"type": "number", "description": "Sunrise time, Unix, UTC."},
            #                         "sunset": {"type": "number", "description": "Sunset time, Unix, UTC."}
            #                     }
            #                 }
            #             }
            #         }
            #     }
            # },
            # {
            #     "name": "get_air_pollution",
            #     "module": "meteorology",
            #     "description": "Get air pollution index and pollutant levels for a location, at the current moment.",
            #     "response_format": ["json"],
            #     "parameters": {
            #         "type": "object",
            #         "properties": {
            #             "lat": {"type": "number", "description": "Latitude (-90 to 90)."},
            #             "lon": {"type": "number", "description": "Longitude (-180 to 180)."},
            #             "city": {"type": "string", "description": "City name."},
            #             "state_code": {"type": "string", "description": "State code (US only)."},
            #             "country_code": {"type": "string", "description": "ISO 3166 country code."},
            #             "zip": {"type": "string", "description": "Postal code."},
            #             "units": {"type": "string", "description": "Temperature unit: kelvin (default), celsius, fahrenheit."},
            #             "lang": {"type": "string", "description": "Language code for weather description (e.g., 'en')."}
            #         },
            #         "description": "Provide either (1) 'lat' and 'lon', or (2) 'zip' and 'country_code', or (3) 'city' (optionally with 'state_code' and 'country_code')."
            #     },
            #     "response_schema": {
            #         "json": {
            #             "type": "object",
            #             "properties": {
            #                 "coord": {
            #                     "type": "array",
            #                     "items": {
            #                         "type": "number"
            #                     },
            #                     "description": "Coordinates from the specified location (latitude, longitude)."
            #                 },
            #                 "list": {
            #                     "type": "array",
            #                     "items": {
            #                         "type": "object",
            #                         "properties": {
            #                             "dt": {"type": "number", "description": "Date and time, Unix, UTC."},
            #                             "main": {
            #                                 "type": "object",
            #                                 "properties": {
            #                                     "aqi": {"type": "number", "description": " Air Quality Index. Possible values: 1, 2, 3, 4, 5. Where 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor."}
            #                                 }
            #                             },
            #                             "components": {
            #                                 "type": "object",
            #                                 "properties": {
            #                                     "co": {"type": "number", "description": "Concentration of CO (Carbon monoxide), μg/m3."},
            #                                     "no": {"type": "number", "description": "Concentration of NO (Nitrogen monoxide), μg/m3."},
            #                                     "no2": {"type": "number", "description": "Concentration of NO2 (Nitrogen dioxide), μg/m3."},
            #                                     "o3": {"type": "number", "description": " Concentration of O3 (Ozone), μg/m3."},
            #                                     "so2": {"type": "number", "description": "Concentration of SO2 (Sulphur dioxide), μg/m3."},
            #                                     "pm2_5": {"type": "number", "description": "Concentration of PM2.5 (Fine particles matter), μg/m3."},
            #                                     "pm10": {"type": "number", "description": "Concentration of PM10 (Coarse particulate matter), μg/m3."},
            #                                     "nh3": {"type": "number", "description": "Concentration of NH3 (Ammonia), μg/m3."}
            #                                 }
            #                             }
            #                         }
            #                     }
            #                 }
            #             }
            #         }
            #     }
            # }
        ]

    def execute_function(self, name: str, args: dict):
        return getattr(self, f"_{name}")(**args)
    
    def __resolve_coordinates(self, **kwargs) -> dict:
        """Get the geocoding information for a given location if not provided directly."""
        if "lat" in kwargs and "lon" in kwargs:
            url = f"{self.__geo_url}/reverse"
            params = {
                "lat": kwargs["lat"],
                "lon": kwargs["lon"],
                "limit": 1,
                "appid": self.__api_key
            }
            data = self._send_resquest(url, params)
            if not data:
                raise ValueError("No results found for the given location.")
            return {
                "lat": kwargs["lat"],
                "lon": kwargs["lon"],
                "city": data[0]["name"],
                "country": data[0]["country"]
            }

        elif "zip" in kwargs and "country_code" in kwargs:
            # Zip geocode lookup
            url = f"{self.__geo_url}/zip"
            params = {
                "zip": f"{kwargs['zip']},{kwargs['country_code']}",
                "appid": self.__api_key
            }
            data = self._send_resquest(url, params)
            if not data:
                raise ValueError("No results found for the given location.")
            return {
                "lat": data["lat"],
                "lon": data["lon"],
                "city": data["name"],
                "country": data["country"]
            }

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
            data = self._send_resquest(url, params)
            if not data:
                raise ValueError("No results found for the given location.")
            return {
                "lat": data[0]["lat"],
                "lon": data[0]["lon"],
                "city": data[0]["name"],
                "country": data[0]["country"]
            }

        else:
            raise ValueError("Insufficient location information. Provide lat/lon, city, or zip + country_code.")
    
    def _get_current_weather(self, **kwargs) -> str:
        info = self.__resolve_coordinates(**kwargs)

        url = f"{self.__data_url}/weather"
        params = {
            "lat": info["lat"],
            "lon": info["lon"],
            "appid": self.__api_key,
            "units": kwargs.get("units", "metric"),
            "lang": kwargs.get("lang", "en")
        }

        response = self._send_resquest(url, params)
        response["city_name"] = info["city"]
        response["country"] = info["country"]
        response["units"] = kwargs.get("units", "metric")
        return self.__format_current_weather(response)
        
    
    def _get_forecast(self, **kwargs) -> str:
        info = self.__resolve_coordinates(**kwargs)

        url = f"{self.__data_url}/forecast"
        params = {
            "lat": info["lat"],
            "lon": info["lon"],
            "appid": self.__api_key,
            "units": kwargs.get("units", "metric"),
            "lang": kwargs.get("lang", "en")
        }

        response = self._send_resquest(url, params)
        response["city_name"] = info["city"]
        response["country"] = info["country"]
        response["units"] = kwargs.get("units", "metric")
        return self.__format_forecast(response)
        
    def _get_air_pollution(self, **kwargs) -> str:
        info = self.__resolve_coordinates(**kwargs)

        url = f"{self.__data_url}/air_pollution"
        params = {
            "lat": info["lat"],
            "lon": info["lon"],
            "appid": self.__api_key
        }

        response = self._send_resquest(url, params)
        response["city_name"] = info["city"]
        response["country"] = info["country"]
        response["units"] = kwargs.get("units", "metric")
        return self.__format_air_pollution(response)
    
    def __format_current_weather(self, response: dict):
        if not response or "weather" not in response:
            return "Sorry, I couldn't retrieve the weather data."
        
        #Location
        location = response.get("city_name")
        country = response.get("country")
        location_str = f"{location}, {country}"

        #Weather
        weather_desc = response["weather"][0].get("description").capitalize()
        weather_icon = response["weather"][0].get("icon")
        icon = f'<img src="{self.__icons}{weather_icon}.png">' if weather_icon else ""

        #Temperatures
        temp = response["main"].get("temp", None)
        feels_like = response["main"].get("feels_like", None)
        unit = self.__units.get(response.get('units'))
        temp_str = f"{temp}{unit} (feels like {feels_like}{unit})"

        # Humidity & Pressure
        humidity = response["main"].get("humidity")
        pressure = response["main"].get("pressure")

        # Wind
        wind_speed = response.get("wind", {}).get("speed")
        wind_deg = response.get("wind", {}).get("deg")

        # Cloudiness
        clouds = response.get("clouds", {}).get("all")

        # Rain/Snow
        rain = response.get("rain", {}).get("1h")
        snow = response.get("snow", {}).get("1h")

        # Sunrise/Sunset
        sunrise = response.get("sys", {}).get("sunrise")
        sunset = response.get("sys", {}).get("sunset")
        timezone = response.get("timezone", 0)
        sunrise_time = datetime.datetime.utcfromtimestamp(sunrise + timezone).strftime('%H:%M') if sunrise else None
        sunset_time = datetime.datetime.utcfromtimestamp(sunset + timezone).strftime('%H:%M') if sunset else None

        # Build message
        report = f"🌤️ **Weather Report for {location_str}**\n"
        report += f"- Condition: {weather_desc} {icon}\n"
        report += f"- Temperature: {temp_str}\n"
        if humidity: report += f"- Humidity: {humidity}%\n"
        if pressure: report += f"- Pressure: {pressure} hPa\n"
        if wind_speed: report += f"- Wind: {wind_speed} m/s"
        if wind_deg: report += f" from {wind_deg}°"
        report += "\n"
        if clouds is not None: report += f"- Cloudiness: {clouds}%\n"
        if rain is not None: report += f"- Rain (last 1h): {rain} mm\n"
        if snow is not None: report += f"- Snow (last 1h): {snow} mm\n"
        if sunrise_time and sunset_time:
            report += f"- Sunrise: {sunrise_time} | Sunset: {sunset_time}\n"

        return report.strip()

    def __format_forecast(self, response: dict):
        if not response or "list" not in response:
            return "Sorry, I couldn't retrieve the forecast data."
        
        #Location
        location = response.get("city_name")
        country = response.get("country")
        location_str = f"{location}, {country}"
        timezone = response.get("city", {}).get("timezone", 0)
        unit = self.__units.get(response.get('units'))

        header = f"📅 5-Day Weather Forecast for {location_str}:\n"
        forecast_list = response["list"]

        report = ""
        for item in forecast_list:
            dt = item.get("dt")
            time_str = datetime.datetime.utcfromtimestamp(dt + timezone).strftime("%d/%m %H:%M") if dt else "Unknown time"
            weather_desc = item["weather"][0].get("description", "No description").capitalize()
            weather_icon = item["weather"][0].get("icon")
            icon = f'<img src="{self.__icons}{weather_icon}.png">' if weather_icon else ""
            temp = item["main"].get("temp")
            report += f"- [{time_str}] {icon} {weather_desc}, {temp}{unit}\n"
        
        return header + report.strip()
    
    def __format_air_pollution(self, response: dict):
        if not response or "list" not in response:
            return "Sorry, I couldn't retrieve the air pollution data."
        
        location = response.get("city_name")
        country = response.get("country")
        location_str = f"{location}, {country}"

        data = response["list"][0]  # Assume first element for current data
        aqi = data.get("main", {}).get("aqi", "Unknown")

        pollutants = data.get("components", {})
        pollutant_strings = []
        for key, value in pollutants.items():
            pollutant_strings.append(f"- {key.upper()}: {value} µg/m³")

        aqi_meaning = {
            1: "Good",
            2: "Fair",
            3: "Moderate",
            4: "Poor",
            5: "Very Poor"
        }.get(aqi, "Unknown")

        report = f"🌬️ Air Quality Report in {location_str}:\n- AQI: {aqi} ({aqi_meaning})\n" + "\n".join(pollutant_strings)

        return report.strip()

