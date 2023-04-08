FROM python:3.11 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./req.txt .

RUN apt update && \
    python3 -m pip install --upgrade pip && \
    pip install -r req.txt
