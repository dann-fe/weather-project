from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['dann1987.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dann1987$default',
        'USER': 'dann1987',
        'PASSWORD': 'imgoodman123',
        'HOST': 'dann1987.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

STATIC_ROOT = BASE_DIR / 'static/'
