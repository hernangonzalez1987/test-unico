# HERNAN GONZALEZ TEST FOR UNICO

REST API for Markets

## Installation

The APIs can be run using docker.

To install docker follow the instructions from https://docs.docker.com/engine/install/.

The API needs a PostgreSQL database to run. To run locally, a dockerized database can be created using the following commands:
- docker pull postgres:9.6.21-alpine
- docker run -e POSTGRES_DB=unico -e POSTGRES_USER=unico -e POSTGRES_PASSWORD=unico -p 5432:5432 -d postgres

To create the database schema the following command should be executed (*):

- docker run -it --network=host api migrate


Optionally to load database with initial data the following command can be executed (*):

- docker run -it --network=host initial_load 


## Usage

To run the API the following command should be executed (*):

- docker run -it --network=host -p 8000:8000 api runserver

The API will be exposed in localhost:8000 once it is running. 


## API Documentation




## Logs

## Test




* To use a different Database from the default,  the following parameters should be add to the docker command:
    -e DBHOST={host} 
    -e DBPORT={port} 
    -e DBNAME={dbName} 
    -e DBUSER={dbUser} 
    -e DBPASS={dbPass} 

  Example : - docker run -e DBHOST={host} -e DBPORT={port} -e DBNAME={dbName} -e DBUSER={dbUser} -e DBPASS={dbPass} -it --network=host initial_load 



Validar DB


Live Demo


Tecnologias utilizadas

Python
Djando
Postgres
Docker
Swagger?
Heroku