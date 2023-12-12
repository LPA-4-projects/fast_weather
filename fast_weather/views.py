from fastapi import APIRouter

from fast_weather.client import WeatherClient
from fast_weather.config import load_config
from fast_weather.schemas import CityWeather

config = load_config()
weather_client = WeatherClient(config.open_weather)

router = APIRouter(
    prefix='/weather',
    tags=['Weather'],
)

@router.get('/')
def get_weather(city: str) -> CityWeather:
    weather_info = weather_client.get_weather_by_city(city)
    return weather_info
