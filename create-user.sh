#!/bin/sh

docker-compose exec web \
    airflow users create \
        -e admin@email.com \
        -f Admin \
        -l Admin \
        -r Admin \
        -p password.123 \
        -u admin
