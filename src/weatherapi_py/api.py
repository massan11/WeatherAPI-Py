from .base import WeatherAPIBase
import requests

class OpenMeteo(WeatherAPIBase):
    def __init__(self, latitude, longitude, **kwargs):
        self.latitude = latitude
        self.longitude = longitude
    
    def get_current_temperature(self):
        params = {"latitude": self.latitude, "longitude": self.longitude, "current_weather": True}
        result = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
        json_result = result.json()
        return json_result["current_weather"]["temperature"]
    
class OpenWeather(WeatherAPIBase):
    def __init__(self, latitude, longitude, **kwargs):
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = kwargs.get("api_key")
        
    def get_current_temperature(self):
        params = {"lat": self.latitude, "lon": self.longitude, "appid": self.api_key}
        result = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
        json_result = result.json()
        return json_result["main"]["temp"]    
    
    def kelvin_to_celsius(self, temp):
        return temp - 273.15
    
    



    

    
    

