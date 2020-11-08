FROM python:3.8-slim-buster

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    wget \
    jq && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY requirements.txt ./requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r ./requirements.txt && \
    python3 -m pip check

RUN wget -q https://github.com/peaceiris/emoji-ime-dictionary/releases/download/v2.2.1/Janome-0.4.1-neologd-20200910.tar.gz && \
    python3 -m pip install --no-cache-dir --no-compile Janome-0.4.1-neologd-20200910.tar.gz && \
    rm Janome-0.4.1-neologd-20200910.tar.gz

RUN wget -q 'https://raw.githubusercontent.com/yagays/emoji-ja/20190726/data/emoji_ja.json' \
      -O /root/emoji_ja.json

WORKDIR /src
