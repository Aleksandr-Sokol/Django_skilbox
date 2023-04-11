#!/bin/sh

python manage.py migrate || exit 1
python manage.py initadmin
python manage.py runserver 0.0.0.0:8080

