# sql_test
Practice with docker, flask, and mysql

## Installation
I'm using this sql database for practice https://www.dropbox.com/s/znmjrtlae6vt4zi/employees.sql?dl=0 </br>
To add it to your server you need to put it in /sql_test/data/employees.sql
or you need to comment out the line in docker-compose db:volumes: - ./data/employees etc

## Run
```
docker-compose up --build -d
```
Then go to localhost:5000
or localhost:8080 to view database

## Troubleshoot Server
```
docker exec -it test_sql mysql -uroot -p
```
password=password
