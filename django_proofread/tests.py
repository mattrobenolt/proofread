import unittest
from django.conf import settings
from django.test.client import Client

ENDPOINTS = getattr(settings, 'PROOFREAD_ENDPOINTS', None)
if ENDPOINTS is None:
    import warnings
    warnings.warn('settings.PROOFREAD_ENDPOINTS is missing')
    ENDPOINTS = {}


class BuildTestCase(type):
    def __new__(cls, name, bases, attrs):
        for endpoint, status_code in ENDPOINTS.items():
            name = 'test_url_%s_%d' % (endpoint, status_code)
            attrs[name] = (lambda endpoint, expected:
                                lambda self:
                                    self.assertEqual(self.client.get(endpoint).status_code, expected)
                          )(endpoint, status_code)
            attrs[name].__name__ = name
            attrs[name].__doc__ = '`%s` should respond with a %d' % (endpoint, status_code)
        return super(BuildTestCase, cls).__new__(cls, name, bases, attrs)


class Endpoints(unittest.TestCase):
    __metaclass__ = BuildTestCase

    def setUp(self):
        self.client = Client()
