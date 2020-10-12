FROM python:3-slim-buster

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /build
COPY requirements.txt ./requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r ./requirements.txt && \
    python3 -m pip check

WORKDIR /src
