# HERNAN GONZALEZ TEST FOR UNICO

REST API for Markets

## Technologies used

 - Python
 - Django 
 - PostgreSQL
 - Heroku

## Installation

The APIs can be run using docker.

To install docker follow the instructions from https://docs.docker.com/engine/install/.

The API needs a PostgreSQL database to run. To run locally, a dockerized database can be created using the following commands:
 - docker pull postgres:9.6.21-alpine
 - docker run -e POSTGRES_DB=unico -e POSTGRES_USER=unico -e POSTGRES_PASSWORD=unico -p 5432:5432 -d postgres

To create the database schema the following command should be executed (*):

 - docker run -it --network=host api migrate


Optionally to load database with initial data the following command can be executed (*):

 - docker run -it -v $PWD:/data --network=host initial_load 

To run sucessfully the file DEINFO_AB_FEIRASLIVRES_2014.csv should be present in the same folder the command is executed.


## Usage

To run the API the following command should be executed (*):

 - docker run -it --rm --network=host --name unico-api api runserver

The API will be exposed in localhost:8000 once it is running. 


## API Documentation

Documentation of the API can be found in:
 
 - {host}/api/schema/swagger-ui/

## Logs

Logs of the API are being save to the file app.log in root folder. To obtain it from docker container the following command can be executed:

 - docker cp $(docker ps -qf "name=unico-api"):/app.log app.log

File "app.log" will be created in the current folder contained the copied logs from docker container.


## Test

In order to run test it is need to to have Python and Pip installed.

To run the tests execute the following commands on root folder :

 - pip install -r requirements.txt
 - sh test.sh

It should print the result of all unit tests and a report with coverage.








* To use a different Database from the default,  the following parameters should be add to the docker command:
    -e DBHOST={host} 
    -e DBPORT={port} 
    -e DBNAME={dbName} 
    -e DBUSER={dbUser} 
    -e DBPASS={dbPass} 

  Example : - docker run -e DBHOST={host} -e DBPORT={port} -e DBNAME={dbName} -e DBUSER={dbUser} -e DBPASS={dbPass} -it --network=host initial_load 



Postman


Live Demo


Tecnologias utilizadas

Python
Djando
Postgres
Docker
Swagger?
Heroku