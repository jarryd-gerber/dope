FROM python:3-alpine

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD . /app
WORKDIR /app
VOLUME /app
