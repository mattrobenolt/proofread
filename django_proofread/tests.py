import unittest
from django.conf import settings
from django.test.client import Client

OK = 200
NOT_FOUND = 404

ENDPOINTS = set()
for key, status in (('SUCCESS', OK), ('FAILURES', NOT_FOUND)):
    for endpoint in getattr(settings, 'PROOFREAD_%s' % key, ()):
        if not endpoint.startswith('/'):
            endpoint = '/' + endpoint
        ENDPOINTS.add((endpoint, status))

if not ENDPOINTS:
    import warnings
    warnings.warn("You haven't specified any urls for Proofread to test!")


class BuildTestCase(type):
    def __new__(cls, name, bases, attrs):
        for endpoint, status_code in ENDPOINTS:
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
