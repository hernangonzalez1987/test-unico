FROM ubuntu:20.04

WORKDIR /

ADD DEINFO_AB_FEIRASLIVRES_2014.csv .
ADD load.* ./
RUN sh ./load.sh

ENTRYPOINT python3 ./load.py

