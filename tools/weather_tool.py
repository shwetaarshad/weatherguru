import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city: str) -> str:
    if not WEATHER_API_KEY:
        return "Weather API key is missing."

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return f"Error: {data.get('message', 'Failed to fetch weather.')}"

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The current weather in {city} is {temp}°C with {desc}."
    except Exception as e:
        return f"Error fetching weather: {str(e)}"
