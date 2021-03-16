FROM python:3.7-buster

WORKDIR /

ADD . .
RUN pip install -r /requirements.txt 

ENTRYPOINT ["python","manage.py"] 