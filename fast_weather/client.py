import httpx

from fast_weather.schemas import CityWeather
from fast_weather.config import OpenweatherConf


class WeatherClient:
    def __init__(self, config: OpenweatherConf) -> None:
        self.config = config

    def get_weather_by_city(self, city: str) -> CityWeather:
        with httpx.Client() as client:
            params = {
                'appid': self.config.api_key,
                'q': city,
                'units': 'metric',
                'lang': 'en',
            }
            response = client.get(url=self.config.url, params=params)
            response.raise_for_status()

            data = response.json()
            return CityWeather(city=city, current_temp=data['main']['temp'])
