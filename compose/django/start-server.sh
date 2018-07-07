#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput

uwsgi --socket :8001 --wsgi-file /app/ara/wsgi.py --py-autoreload 3 -b 16384
