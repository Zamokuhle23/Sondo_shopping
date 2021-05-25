release: python manage.py migrate --noinput
web: gunicorn Sondo_shopping.wsgi
worker: celery -A Sondo_shopping.tasks worker -B --loglevel=info
channelsworker: python manage.py runworker -v2