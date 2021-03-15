# HERNAN GONZALEZ TEST FOR UNICO

REST API for Markets

## Installation

The APIs can be run using docker or directly using python scripts.

To install docker follow the instructions from https://docs.docker.com/engine/install/.

The API needs a PostgreSQL database to run. To run locally, a dockerized database can be created using the following commands:
- docker pull postgres:9.6.21-alpine
- docker run -e POSTGRES_DB=unico -e POSTGRES_USER=unico -e POSTGRES_PASSWORD=unico -p 5432:5432 -d postgres

To load database with initial data the following command can be run:

- docker run -it --network=host initial_load 

By default the local Database created will be used. To use another one add the following parameters:

- docker run -e DBHOST={host} -e DBPORT={port} -e DBNAME={dbName} -e DBUSER={dbUser} -e DBPASS={dbPass} -it --network=host initial_load 

## Usage

To run the dockerized version of the API the following command should be run:

- docker run -it --network=host -p 8000:8000 api runserver

The API will be exposed in port 8000 once it is running. 

By default the local Database created will be used. To use another one add the following parameters:

- docker run -e DBHOST={host} -e DBPORT={port} -e DBNAME={dbName} -e DBUSER={dbUser} -e DBPASS={dbPass} -it --network=host -p 8000:8000 api runserver

## API Documentation


## Logs

## Test
