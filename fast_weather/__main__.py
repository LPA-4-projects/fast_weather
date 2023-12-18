from fast_weather.app import create_app
from fast_weather.config import load_config


def main() -> None:
    config = load_config()
    import uvicorn  # noqa: WPS433

    app = create_app()
    uvicorn.run(app=app, host=config.web.host, port=config.web.port)


if __name__ == '__main__':
    main()
