FROM ubuntu:20.04

WORKDIR /

ADD load.* ./
RUN sh ./load.sh

ENTRYPOINT python3 ./load.py