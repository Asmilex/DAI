from python:3.9-alpine

workdir /app
copy . /app
run pip install -r requirements.txt

env FLASK_APP app.py
env FLASK_RUN_HOST 0.0.0.0
env FLASK_ENV development

cmd ["flask", "run"]