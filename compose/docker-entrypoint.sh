#!/bin/sh
flask db migrate
flask db upgrade

flask run --port 5000 --host 0.0.0.0

# Start Gunicorn processes
# exec gunicorn config.wsgi:app \
#     --name britecore_web \
#     --bind 0.0.0.0:8000 \
#     --workers 3 \
#     --log-level=info \
#     "$@"
