from fast_weather.config import load_config
from fast_weather.server import create_app


def main() -> None:
    config = load_config()
    import uvicorn

    app = create_app()
    uvicorn.run(app=app, host=config.web.host, port=config.web.port)


if __name__ == '__main__':
    main()
