-include .env
export

run:
	@uvicorn fast_weather.app:app --host 0.0.0.0 --port 8000

test:
	@pytest

lint:
	@mypy .
	@flake8 .
