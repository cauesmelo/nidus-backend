FROM python:3.9

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root --no-dev

COPY ./backend /app/backend

ENTRYPOINT [ "uvicorn", "backend.app:app", "--reload", "--port", "8080", "--host", "0.0.0.0" ]
