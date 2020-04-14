#!/bin/bash
if [ "$FLASK_ENV" = 'development' ]; then
    echo "Running Development Server"
    exec python -m flask run --host=0.0.0.0 --port=$FLASK_RUN_PORT
elif [ "$FLASK_ENV" = 'production' ]; then
    echo "Running Production Server"
    exec gunicorn --timeout 30 --workers 1 --bind :$PORT "demo_site:create_app('production')"
else
    echo "No environment selected"
    exit 1
fi
