#!/bin/sh
set -xe

python manage.py makemigrations --no-input
python manage.py migrate --no-input

rm -rf /app/static/*
python manage.py collectstatic --no-input

gunicorn --bind :8000 --workers 3 proyecto.wsgi
