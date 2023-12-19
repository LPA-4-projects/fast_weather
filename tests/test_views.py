from http import HTTPStatus
from unittest.mock import Mock

from fastapi.testclient import TestClient
from httpx import HTTPStatusError, Request, Response

from fast_weather.schemas import CityWeather


def test__get_weather__return_current_weather_if_ok_response(
    test_client: TestClient,
    weather_client_mock: Mock,
    city_weather: CityWeather,
):
    weather_client_mock.get_weather_by_city.return_value = city_weather

    response = test_client.get('/weather/', params={'city': city_weather.city})

    assert response.status_code == 200
    assert response.json()['city'] == city_weather.city


def test__get_weather__return_wrong_city_error_if_not_found_returned_from_weather_client(
    test_client: TestClient,
    weather_client_mock: Mock,
    faker,
):
    weather_client_mock.get_weather_by_city.side_effect = HTTPStatusError(
        'Error',
        request=Request(method='get', url='http://testurl'),
        response=Response(status_code=HTTPStatus.NOT_FOUND),
    )

    response = test_client.get('/weather/', params={'city': faker.pystr()})

    assert response.status_code == 404


def test__get_weather__return_internal_error_if_error_returned_from_weather_client(
    test_client: TestClient,
    weather_client_mock: Mock,
    faker,
):
    weather_client_mock.get_weather_by_city.side_effect = HTTPStatusError(
        'Error',
        request=Request(method='get', url='http://testurl'),
        response=Response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR),
    )

    response = test_client.get('/weather/', params={'city': faker.pystr()})

    assert response.status_code == 500
