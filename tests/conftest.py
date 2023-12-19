from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from fast_weather.app import create_app
from fast_weather.client import WeatherClient, get_weather_client
from fast_weather.config import AppConf, load_config
from fast_weather.schemas import CityWeather


@pytest.fixture
def app_conf_mock():
    with patch('fast_weather.config.load_config') as mock:
        yield mock


@pytest.fixture
def app_config():
    return load_config()


@pytest.fixture
def weather_client(app_config: AppConf):
    return WeatherClient(app_config.open_weather)


@pytest.fixture
def current_temperature(faker):
    return faker.pyfloat(min_value=-50, max_value=40)


@pytest.fixture
def city_weather(current_temperature, faker):
    def inner(city: str | None = None) -> CityWeather:
        city = city or faker.city()
        return CityWeather(
            city=city,
            current_temp=current_temperature,
        )
    return inner()


@pytest.fixture(scope='session')
def weather_client_mock(session_mocker: MockerFixture):
    return session_mocker.Mock(WeatherClient)


@pytest.fixture(scope='session')
def test_client(weather_client_mock):
    app = create_app()
    app.dependency_overrides[get_weather_client] = lambda: weather_client_mock

    with TestClient(app) as client:
        yield client
