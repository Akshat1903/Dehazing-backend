release: python manage.py makemigrations && python manage.py migrate
web: gunicorn dehazing_app_backend.wsgi