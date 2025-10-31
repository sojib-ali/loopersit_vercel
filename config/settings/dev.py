from .base import *

SECRET_KEY = 'django-insecure-3k3ohvn+(eyg5&)^x!-679^18!+ysue5q^c8!-9lr(5ya)_x-#'

DEBUG = True

ALLOWED_HOSTS = []

# Database


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'litdb',
        'USER': 'postgres',
        'PASSWORD': '1294',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'