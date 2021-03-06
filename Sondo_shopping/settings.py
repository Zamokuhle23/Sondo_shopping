"""
Django settings for Sondo_shopping project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import django_heroku
import dj_database_url
import os
from urllib.parse import urljoin

from celery.backends import redis
from channels import staticfiles
from channels_redis.core import RedisChannelLayer
from django.template.context_processors import static
from pip._vendor.cachecontrol.caches import redis_cache, RedisCache


LOGIN_REDIRECT_URL = ('/')


#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Sondo_shopping.settings")
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qwerty123@'
#SECRET_KEY = os.environ.get('SECRET_KEY', '1234')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'customers',
    'store',
    'django_celery_results',
    'rest_framework',
    'rest_framework_swagger',
    'channels',
    'crispy_forms',
    'rest_auth',
    'djcelery_email',
    'celery',


]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'Sondo_shopping.urls'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Sondo_shopping.wsgi.application'
ASGI_APPLICATION = "Sondo_shopping.asgi.application"



CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
MEDIA_URL = '/media/image/'
MEDIA_ROOT = BASE_DIR

# BROKER_URL = os.environ['REDIS_URL']
# CELERY_RESULT_BACKEND = os.environ['REDIS_URL']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'djsbusiso2021@gmail.com'
EMAIL_HOST_PASSWORD = 'taqqlnaidwaoqwoj'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Sondo Online team, Do not Reply to this email'
CELERY_EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'


# r = redis.from_url(os.environ.get("REDIS_URL"))
# BROKER_URL = redis.from_url(os.environ.get("REDIS_URL"))
# CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL')


CELERY_BROKER_URL = "redis://:pfda0000f041c8db9b7945da412c90663ff5b71548151e3b762badbb829ffa872@ec2-54-221-218-75.compute-1.amazonaws.com:11530"
REDIS_URL = "redis://:pfda0000f041c8db9b7945da412c90663ff5b71548151e3b762badbb829ffa872@ec2-54-221-218-75.compute-1.amazonaws.com:11530"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Canada/Eastern'

#redis_url = urljoin(os.environ.get('REDIS_URL'))




# celery setting.
# CELERY_CACHE_BACKEND = 'default'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )


django_heroku.settings(locals())
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'