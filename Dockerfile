FROM python:3.8

LABEL maintainer="omerdemirarsln@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/