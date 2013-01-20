import sys
import os.path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

SECRET_KEY = 'lol'
ROOT_URLCONF = 'tests.urls'
WSGI_APPLICATION = 'tests.wsgi.application'

INSTALLED_APPS = (
    'django_proofread',
)

TEMPLATE_DIRS = 'templates/',

PROOFREAD_SUCCESS = (
    '/',
    'thisisawesome/',
)

PROOFREAD_FAILURES = (
    '/lolidontexist',
    'idontexisteither'
)
