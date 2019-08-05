FROM python:3.7.4-alpine3.10

ENV DATASET_TAG="20190726"
ENV DATASET_URL="https://raw.githubusercontent.com/yagays/emoji-ja/${DATASET_TAG}/data/emoji_ja.json"
WORKDIR /data
RUN wget ${DATASET_URL}

WORKDIR /work
ENV LANG="ja_JP.UTF-8"
ENV MAGENTA_BG="\[\e[0;45m\]"
ENV MAGENTA_FG="\[\e[0;35m\]"
ENV YELLOW_FG="\[\e[0;33m\]"
ENV COLOR_END="\e[m"
ENV PS1="${YELLOW_FG}\w${COLOR_END}\n\
${MAGENTA_BG}docker${COLOR_END}${MAGENTA_FG} > ${COLOR_END}"
COPY requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

CMD [ "./generate.py" ]
ENTRYPOINT [ "python3" ]
