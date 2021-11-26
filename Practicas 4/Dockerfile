FROM python:3.9-alpine
WORKDIR /app
COPY . /app/
RUN apk add build-base zlib-dev jpeg-dev && pip install -r requirements.txt