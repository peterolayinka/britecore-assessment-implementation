#!/bin/sh
flask db upgrade

flask run

# Start Gunicorn processes
# exec gunicorn config.wsgi:application \
#     --name quizboot_web \
#     --bind 0.0.0.0:8000 \
#     --workers 3 \
#     --worker-class="egg:meinheld#gunicorn_worker" \
#     --log-level=info \
#     "$@"
