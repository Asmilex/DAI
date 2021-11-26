```
docker-compose up

docker-compose run web python manage.py startapp galerias
docker-compose run web python manage.py makemigrations galerias
docker-compose run web python manage.py migrate galerias
```