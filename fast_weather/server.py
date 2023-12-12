from fastapi import FastAPI

from fast_weather.views import router as weather_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(weather_router)
    return app
