release: python manage.py migrate --noinput
web: daphne Sondo_shopping.asgi:application --port $PORT --bind 0.0.0.0
worker: celery -A Sondo_shopping.tasks worker -B --loglevel=info
channelsworker: python manage.py runworker -v2