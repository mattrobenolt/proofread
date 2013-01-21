import sys
import os.path

CWD = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.insert(0, CWD)

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
    'proofread.contrib.django_proofread',
)

TEMPLATE_DIRS = os.path.join(CWD, 'tests/templates/'),

PROOFREAD_SUCCESS = (
    '/',
    'thisisawesome/',
)

PROOFREAD_FAILURES = (
    '/lolidontexist',
    'idontexisteither'
)

PROOFREAD_ENDPOINTS = (
    ('/post/', 200, 'POST', {'': 'yep'}),
    ('/post/', 405, 'GET'),
    ('/',)  # Redundant, but making sure the defaults get filled in properly
)
