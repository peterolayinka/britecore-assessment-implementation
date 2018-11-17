#!/bin/sh
flask db migrate
flask db upgrade

# Start Gunicorn processes
exec gunicorn config.wsgi:application \
    --name quizboot_web \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    "$@"
