import httpx

from fast_weather.config import OpenweatherConf, load_config
from fast_weather.schemas import CityWeather


class WeatherClient:
    def __init__(self, config: OpenweatherConf) -> None:
        self.config = config
        self.client = httpx.Client()

    def get_weather_by_city(self, city: str) -> CityWeather:
        with self.client as client:
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


def get_weather_client() -> WeatherClient:
    config = load_config()
    return WeatherClient(config.open_weather)
