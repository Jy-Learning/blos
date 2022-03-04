FROM python:3.10
RUN pip install 'poetry==1.1.12'
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
COPY . .
CMD gunicorn -c ./gunicorn.conf.py blos.main:app