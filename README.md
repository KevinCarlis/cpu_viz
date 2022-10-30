# CPU Visualizer
A 1 byte CPU simulator

## Installation
You will need to install <a href="https://www.docker.com">docker<a>
<br/>
You can install docker on your local machine through the command line apt-get,
but I personally use Docker Desktop with WSL

## Run
From the root of the project folder
use the command line to create the docker container
from the docker-compose.yml
```
docker-compose up --build -d
```
Then go to your web browser and type localhost:5000 into the address bar

## Exiting
After you're done you can close your docker container with
```
docker-compose down
```
