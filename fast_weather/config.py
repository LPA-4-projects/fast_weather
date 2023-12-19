from os import getenv
from typing import Any

from dotenv import load_dotenv
from pydantic import BaseModel


class WebConf(BaseModel):
    host: str
    port: int


class OpenweatherConf(BaseModel):
    api_key: str
    url: str


class AppConf(BaseModel):
    web: WebConf
    open_weather: OpenweatherConf


config: dict[str, Any] = {
    'web': {
        'host': getenv('APP_HOST', '0.0.0.0'),
        'port': int(getenv('APP_PORT', '8000')),
    },
    'open_weather': {
        'api_key': getenv('API_KEY', ''),
        'url': getenv('OPENWEATHER_URL', ''),
    },
}


def load_config() -> AppConf:
    load_dotenv()
    return AppConf(**config)
