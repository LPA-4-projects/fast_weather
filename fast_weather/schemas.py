from pydantic import BaseModel


class CityWeather(BaseModel):
    city: str
    current_temp: float
