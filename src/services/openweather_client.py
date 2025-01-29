import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from src.models.weather_data import WeatherData


class OpenWeatherMapClient:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, location: str, unit: str):
        params = {
            "q": location,
            "units": unit,
            "appid": self.api_key
        }
        response = requests.get(self.base_url, params=params) # sends HTTP GET request to API
        response.raise_for_status() # Checks HTTP response status code. If 200(success) continue, else HTTPError
        data = response.json()
        #extraction:
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        condition = data["weather"][0]["main"]  # e.g., "Clear", "Clouds"
        sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.utcfromtimestamp(data["sys"]["sunset"])
        timezone_offset = data["timezone"]  # in seconds
        timezone = f"UTC{timezone_offset/3600:+.1f}"
        return WeatherData(
            temperature=temperature,
            feels_like=feels_like,
            humidity=humidity,
            wind_speed=wind_speed,
            condition=condition,
            sunrise=sunrise,
            sunset=sunset,
            timezone=timezone
        )

#simple test
if __name__ == "__main__":
    load_dotenv()
    client = OpenWeatherMapClient()
    weather_data = client.get_weather_data("London", "metric")
    print(weather_data.to_dict())
