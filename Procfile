release: python manage.py makemigrations && python manage.py migrate
web: gunicorn dehazing_app_backend.wsgi
worker: celery -A dehazing_app_backend worker -l info