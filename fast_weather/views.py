from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from httpx import HTTPStatusError

from fast_weather.client import get_weather_client, WeatherClient
from fast_weather.schemas import CityWeather

router = APIRouter(
    prefix='/weather',
    tags=['Weather'],
)

@router.get('/')
def get_weather(
    city: str,
    client: WeatherClient = Depends(get_weather_client),
) -> CityWeather:
    try:
        weather_info = client.get_weather_by_city(city)
    except HTTPStatusError as error:
        code = error.response.status_code
        if code == HTTPStatus.NOT_FOUND:
            raise HTTPException(
                status_code=code,
                detail='City not found',
            )
        raise HTTPException(
            status_code=code,
            detail='Weather server return an error'
        )

    return weather_info
