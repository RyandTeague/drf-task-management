release: python manage.py makemigrations && python manage.py migrate

web: gunicorn drf_tsk.wsgi
