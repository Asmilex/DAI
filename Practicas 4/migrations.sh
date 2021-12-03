#!/bin/bash
docker-compose run web python manage.py makemigrations galerias
docker-compose run web python manage.py migrate galerias