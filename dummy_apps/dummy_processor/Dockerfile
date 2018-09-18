FROM python:3.6.6-alpine3.8

WORKDIR /processor

RUN pip install pipenv

COPY Pipfile ./

RUN pipenv install

COPY src .

ENTRYPOINT ["pipenv", "run", "python", "task.py"]
