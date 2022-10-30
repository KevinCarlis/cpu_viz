# CPU Visualizer
A 1 byte CPU simulator

## Installation
You will need to install <a href="https://www.docker.com">docker<a>
<br/>
I use Docker Desktop with WSL personally

## Run
From the root of the project folder
use the command line to create the docker container
from the docker-compose.yml
```
docker-compose up --build -d
```
Then go to your web browser and type localhost:5000 into the address bar

## Troubleshoot Server
```
docker exec -it test_sql mysql -uroot -p
```
