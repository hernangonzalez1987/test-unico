docker build -t initial_load .
docker run -v $PWD:/data --network=host initial_load