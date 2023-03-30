#!/bin/bash
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py initadmin
python manage.py collectstatic --no-input
python manage.py loaddata testdata.json

TIMEOUT=120

exec python manage.py runserver 0.0.0.0:8000