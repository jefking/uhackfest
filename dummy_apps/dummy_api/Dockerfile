FROM python:3.6.6-alpine3.8

WORKDIR /api

RUN pip install pipenv

COPY Pipfile ./

RUN pipenv install

COPY src .

CMD ["pipenv", "run", "gunicorn", "-w 4", "-b 0.0.0.0:8000", "app:app"]
