FROM python:3.7-buster

WORKDIR /

ADD load.* ./
RUN sh ./load.sh

ENTRYPOINT python3 ./load.py