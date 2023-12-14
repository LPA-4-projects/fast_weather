# fast_weather

A simple FastAPI app for gathering a weather forecast

## Development

Create a virtual environment

```bash
poetry shell
```

Install dependencies

```bash
poetry install
```

Create a `.env` file from the `.env.template` and fill it with your creds

## Run

Local run

```bash
make run
```

Docker run (you must have Docker already installed on your machine)

```bash
docker compose up -d app
```

Test it

```bash
curl http://localhost:8000/weather/?city=Moscow
```
