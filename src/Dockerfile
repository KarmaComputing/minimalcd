FROM python:3.10-alpine

WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN apk add --update --no-cache build-base \
    libffi-dev openssl-dev bash git gcc sqlite \
    curl
