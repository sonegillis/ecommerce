from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ['localhost', ]
CORS_ORIGIN_WHITELIST = ('http://localhost:8100',)
