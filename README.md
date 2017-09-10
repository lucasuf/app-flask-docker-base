## Dockerizing Flask With Compose and Machine - From Localhost to the Cloud - Lucas Barros and Felipe Fernandes

Steps:
1. First initializing docker-machine
$ docker-machine create -d virtualbox dev;

2. Eval VM
$ eval "$(docker-machine env dev)"

3. Run docker-compose
$ docker-compose build
$ docker-compose up -d

4. Create the database table
$ docker-compose run web /usr/local/bin/python create_db.py




