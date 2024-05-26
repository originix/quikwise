FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/

WORKDIR /app/

COPY requirements.txt /app/

RUN apk add --update --no-cache bash mariadb-connector-c jpeg-dev gettext

RUN apk add --no-cache --virtual .build-deps python3-dev musl-dev mariadb-dev libffi-dev openssl-dev build-base

RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .build-deps

RUN mkdir -p /app/

WORKDIR /app/

COPY . /app/

COPY ./start-gunicorn /start-gunicorn
RUN chmod +x /start-gunicorn

COPY ./start-celeryworker /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./start-celerybeat /start-celerybeat
RUN chmod +x /start-celerybeat

EXPOSE 5000

CMD ["/start-gunicorn"]
