-include .env
export

run:
	@uvicorn fast_weather.server:create_app --host 0.0.0.0 --port 8000
