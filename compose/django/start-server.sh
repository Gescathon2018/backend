#!/bin/sh
python manage.py migrate

uwsgi --socket :8001 --wsgi-file /app/backend/wsgi.py --py-autoreload 3 -b 16384
