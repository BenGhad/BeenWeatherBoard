from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os

from src.controllers.weather_controller import WeatherController

# Load environment variables
load_dotenv()

app = FastAPI(title="Weather Dashboard")

# Create a single, shared WeatherController instance
weather_controller = WeatherController()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return """
    <html>
      <head><title>Welcome!</title></head>
      <body>
        <h1>Welcome to my Weather Dashboard!</h1>
        <p>Try <a href="/weather?location=London&unit=metric">/weather?location=London&unit=metric</a></p>
      </body>
    </html>
    """

@app.get("/weather")
def get_weather(location: str, unit: str = "metric"):
    """
    Endpoint: /weather?location=London&unit=metric
    """
    try:
        weather_data = weather_controller.get_weather(location, unit)
        return weather_data.to_dict()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
