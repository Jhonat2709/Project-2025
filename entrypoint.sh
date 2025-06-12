#!/usr/bin/env bash 
# This exits on error
set -o errexit

# Collect static files
python manage.py collectstatic --no-input

# Migrate the database
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# Create indexes for search functionality
python manage.py rebuild_index --noinput

# Execute the application using Gunicorn with Uvicorn worker
exec gunicorn -b 0.0.0.0:8000 sapient_unefa.wsgi:application