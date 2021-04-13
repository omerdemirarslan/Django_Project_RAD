FROM python:3.9-alpine

LABEL maintainer="omerdemirarsln@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Install postgres client
RUN apk add --update --no-cache postgresql-client jpeg-dev

# Install individual dependencies so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps


COPY . /app

WORKDIR /app
