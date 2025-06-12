#!/usr/bin/env bash 
# This exits on error
set -o errexit

# Install dependencies
pip install --no-cache-dir -r requirements.txt

# Compile staticfiles
python manage.py collectstatic --no-input

# Migrate the database
python manage.py makemigrations --no-input
python manage.py migrate --no-input

# Create indexes for search functionality
python manage.py rebuild_index --noinput