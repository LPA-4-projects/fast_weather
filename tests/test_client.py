from unittest.mock import Mock

import pytest
from httpx import HTTPStatusError
from pytest_httpx import HTTPXMock

from fast_weather.client import WeatherClient, get_weather_client
from fast_weather.config import AppConf


def test__get_weather_by_city__can_return_weather(
    current_temperature: float,
    weather_client: WeatherClient,
    httpx_mock: HTTPXMock,
):
    httpx_mock.add_response(status_code=200, json={
        "main": {
            "temp": current_temperature,
        },
    })

    response = weather_client.get_weather_by_city(city='Moscow')

    assert response.current_temp == current_temperature


def test__get_weather_by_city__raise_error_if_not_ok_response(
    weather_client: WeatherClient,
    httpx_mock: HTTPXMock,
):
    httpx_mock.add_response(status_code=404)

    with pytest.raises(HTTPStatusError):
        weather_client.get_weather_by_city(city='Moscow')


def test__get_weather_client__correctly_return_client(
    app_conf_mock: Mock,
    app_config: AppConf,
):
    app_conf_mock.return_value = app_config

    client = get_weather_client()

    assert isinstance(client, WeatherClient)
    assert client.config.url == app_config.open_weather.url
