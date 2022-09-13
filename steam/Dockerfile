# Pull base image
FROM python:3.8.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -yyq netcat

# Set work directory
WORKDIR /usr/src/app/

COPY Pipfile* /usr/src/app/
RUN pip install pipenv && pipenv install --deploy --system --ignore-pipfile

COPY . /usr/src/app

CMD ./entrypoint.sh