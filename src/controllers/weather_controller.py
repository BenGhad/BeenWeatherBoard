from dotenv import load_dotenv

from src.services.openweather_client import OpenWeatherMapClient
from src.services.cache_manager import InMemoryCacheManger
from src.models.weather_data import WeatherData

class WeatherController:
    def __init__(self, api_client=None, cache_manager=None):
        self.api_client = api_client or OpenWeatherMapClient()
        self.cache_manager = cache_manager or InMemoryCacheManger()

    def get_weather(self, location: str, unit: str = "metric") -> WeatherData:
        # Checks cache, then calls weather API
        if self.cache_manager.is_cache_valid(location):
            return self.cache_manager.get_cached_data(location)
        else:
            weather_data = self.api_client.get_weather_data(location, unit)
            self.cache_manager.set_cached_data(location, weather_data)
            return weather_data



if __name__ == "__main__":
    load_dotenv()
    controller = WeatherController()
    print("First call (API fetch):")
    data = controller.get_weather("London")
    print(data.to_dict())

    print("Second call (cache fetch):")
    data2 = controller.get_weather("London")
    print(data2.to_dict())
