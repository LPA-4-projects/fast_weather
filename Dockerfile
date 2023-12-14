FROM python:3.11-slim

ENV PYTHONUNBUFFERED=True \
    POETRY_VIRTUALENVS_CREATE=False

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

COPY fast_weather /app/fast_weather

CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "8000", "fast_weather.app:app"]
