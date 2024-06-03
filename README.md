# quikwise
Quikwise is a team workspace where knowledge and collaboration meet.

###### How To run this project

**note please install docker and docker-compose before run this project

###### How to run
```sh
# Build docker image
$ docker-compose build

# Run service
$ docker-compose up -d

# Migrate database
$ docker-compose exec quikwise python manage.py migrate
$ docker-compose exec quikwise python manage.py fix_utf8

# Run test
$ docker-compose exec quikwise coverage run manage.py test
$ docker-compose exec quikwise coverage report

# Bring system down without destroy any data
$ docker-compose down

# Bring system down AND DESTROY ALL DATA
$ docker-compose down --volumes
```

