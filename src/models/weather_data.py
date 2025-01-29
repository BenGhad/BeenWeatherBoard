from datetime import datetime

class WeatherData:
    def __init__(self, temperature, feels_like, humidity, wind_speed, condition, sunrise, sunset, timezone):
        self.temperature = temperature
        self.feels_like = feels_like
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.condition = condition
        self.sunrise = sunrise
        self.sunset = sunset
        self.timezone = timezone


    def to_dict(self):
        return {
            "temperature": self.temperature,
            "feels_like": self.feels_like,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed,
            "condition": self.condition,
            "sunrise": self.sunrise.isoformat() if isinstance(self.sunrise, datetime) else self.sunrise,
            "sunset": self.sunset.isoformat() if isinstance(self.sunset, datetime) else self.sunset,
            "timezone": self.timezone
        }