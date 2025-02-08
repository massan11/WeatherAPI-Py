# WeatherAPI-Py 🌍☁️  
A Python package for retrieving real-time air temperature from Open-Meteo and OpenWeather APIs. Supports multiple APIs, easy integration, and includes Kelvin-to-Celsius conversion for OpenWeather.

## 🌟 Features  
- ✅ Supports Open-Meteo & OpenWeather APIs  
- ✅ Object-oriented architecture for easy extension  
- ✅ Kelvin to Celsius conversion for OpenWeather  
- ✅ Lightweight and easy to use  

## 🚀 Installation  
```bash
pip install weatherapi-py

📌 Usage

from weatherapi import OpenMeteo, OpenWeather

# Using Open-Meteo
open_meteo = OpenMeteo(35.6944, 51.4215)
temperature = open_meteo.get_current_temperature()
print(f"Temperature from Open-Meteo: {temperature}°C")

# Using OpenWeather (requires API key)
open_weather = OpenWeather(35.6944, 51.4215, api_key="your_api_key")
temperature = open_weather.get_current_temperature()
temperature = open_weather.kelvin_to_celsius(temperature)
print(f"Temperature from OpenWeather: {temperature}°C")

📜 License
This project is licensed under the MIT License.