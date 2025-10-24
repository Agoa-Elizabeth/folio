#!/usr/bin/env bash
set -o errexit
python manage.py collectstatic --noinput
python manage.py migrate

set -o errexit

echo "Starting build process..."

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Running migrations..."
python manage.py migrate --noinput

echo "Build complete!"