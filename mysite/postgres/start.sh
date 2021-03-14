docker pull postgres:9.6.21-alpine
docker run -e POSTGRES_DB=unico -e POSTGRES_USER=unico -e POSTGRES_PASSWORD=unico -p 5432:5432 -d postgres