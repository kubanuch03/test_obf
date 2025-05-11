# Start Migrations processes
echo run Pyarmor


# Start Gunicorn processes
echo Starting Server
poetry run python manage.py runserver 0.0.0.0:8989
