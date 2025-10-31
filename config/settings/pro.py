from .base import *
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qsl

load_dotenv()

tmpPostgres = urlparse(os.getenv("DATABASE_URL"))


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False


# ADMINS = (
#     ('Sarwar Zahan', 'zahan.ads@gmail.com'),
# )


ALLOWED_HOSTS = ['loopersit-final.onrender.com', 'loopersit.com', 'www.loopersit.com']

INSTALLED_APPS += ["cloudinary_storage", "cloudinary"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': tmpPostgres.path.replace('/', ''),
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
        'OPTIONS': dict(parse_qsl(tmpPostgres.query)),
    }
}

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.environ.get("CLOUDINARY_API_KEY"),
    "API_SECRET": os.environ.get("CLOUDINARY_API_SECRET"),
}

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage"
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    }
}

MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://res.cloudinary.com/dui0mqbio/image/upload/v1/{MEDIA_LOCATION}/'

EMAIL_HOST_USER = 'szahan4@gmail.com' 


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
# MEDIA_URL = 'https://plant-trends.bsmiab.org/media/'