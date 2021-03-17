# HERNAN GONZALEZ TEST FOR UNICO

REST API for Markets

## Made using

- Python
- Django
- PostgreSQL
- Heroku Cloud

## Live Demo & API documentation

A live demo of the API and the documentation can be found in the following link:

https://test-unico.herokuapp.com/api/schema/swagger-ui/

## Installation

### Requirements:

If you do not have Docker installed, you can do it following the instructions from https://docs.docker.com/engine/install/.

To install Python and Pip follow the instructions from https://docs.python-guide.org/starting/installation/


### Docker images:
The API is available in DockerHub. To get the images run the following commands:

- docker pull hernangonzalez1987/test-unico
- docker pull hernangonzalez1987/test-unico-load


### Database:
The API needs a PostgreSQL database to run. A dockerized database can be created using the following commands:

- docker pull postgres:9.6.21-alpine
- docker run -e POSTGRES_DB=unico -e POSTGRES_USER=unico -e POSTGRES_PASSWORD=unico -p 5432:5432 -d postgres

> A default Database with Name, User and Password "unico" will be created. To use a different one, you should create the Database and define the following environment variables DBHOST, DBPORT, DBNAME, DBUSER,DBPASS with the configuration.
> Also, in case the application is being run using Docker, the proper parameters should be added to any Docker command.
> Example : - docker run -e DBHOST={host} -e DBPORT={port} -e DBNAME={dbName} -e DBUSER={dbUser} -e DBPASS={dbPass} -it --network=host initial_load

Before executing the Application for the first time, it is needed to create the database schema. In order to do that the following command should be executed (\*):

- #### With Docker:

  - docker run -it --network=host hernangonzalez1987/test-unico migrate

- #### With Script (from root folder):
  - pipenv shell
  - ./manage.py migrate

Optionally, to load database with initial data the following command can be executed (\*):

- docker run -it -v $PWD:/data --network=host hernangonzalez1987/test-unico-load

To run sucessfully the file DEINFO_AB_FEIRASLIVRES_2014.csv should be present in the same folder the command is executed.
It can be found inside "initial_load" folder

## Usage

To run the API the following command should be executed (\*):

- #### With Docker:

  - docker run -it --rm --network=host -v $PWD/logs:/logs --name unico-api hernangonzalez1987/test-unico runserver

- #### With Script (from root folder, still in venv):
  - ./manage.py runserver

The API will be exposed in localhost:8000 once it is running.

## Postman

A Postman collection with example requests and responses is included in the folder "postman" .

## Logs

Logs are stored in folder "logs" in the file "app.log"

## Test

To run the tests execute the following commands on root folder (still from venv):

- sh test.sh

It will print the result of all unit tests and a report with coverage.
