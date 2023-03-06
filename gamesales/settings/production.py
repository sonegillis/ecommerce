from .base import *
import environ

env = environ.Env()

environ.Env.read_env(os.path.join(BASE_DIR / ".env"))

STATIC_ROOT = "staticfiles"

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
