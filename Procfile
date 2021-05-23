release: python manage.py migrate --noinput
web: daphne Sondo_shopping.asgi:application --port $PORT --bind 0.0.0.0
worker: REMAP_SIGTERM=SIGQUIT celery worker --app Sondo_shopping.celery.app --loglevel info