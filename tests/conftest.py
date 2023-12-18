from unittest.mock import patch

import pytest

from fast_weather.client import WeatherClient
from fast_weather.config import load_config


@pytest.fixture
def app_conf_mock():
    with patch('fast_weather.config.load_config') as mock:
        yield mock


@pytest.fixture
def app_config():
    return load_config()


@pytest.fixture
def weather_client(app_config) -> WeatherClient:
    return WeatherClient(app_config.open_weather)


@pytest.fixture
def current_temperature(faker):
    return faker.pyfloat(min_value=-50, max_value=40)
