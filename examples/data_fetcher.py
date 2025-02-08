from weatherapi_py.api import OpenMeteo, OpenWeather

open_meteo_obj = OpenMeteo(35.6944, 51.4215)
temp = open_meteo_obj.get_current_temperature()
print(temp)

open_weather_obj = OpenWeather(35.6944, 51.4215, api_key="your_api_key")
temp = open_weather_obj.get_current_temperature()
temp = open_weather_obj.kelvin_to_celsius(temp)
print(temp)
