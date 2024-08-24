docker build --pull --rm -f  "$(pwd)/Dockerfile" -t siuadmin:latest "$(pwd)/docker_test"
docker rmi test123 -f 
docker build -t test123 .