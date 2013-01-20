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
            test_name = 'test_proofread: GET %d %s' % (status_code, endpoint)
            def make_test(endpoint, status_code):
                def run(self):
                    self.assertEqual(self.client.get(endpoint).status_code, status_code)
                return run
            test = make_test(endpoint, status_code)
            test.__name__ = name
            test.__doc__ = '`%s` should respond with a %d' % (endpoint, status_code)
            attrs[test_name] = test
        return super(BuildTestCase, cls).__new__(cls, name, bases, attrs)


class Endpoints(unittest.TestCase):
    __metaclass__ = BuildTestCase

    def setUp(self):
        self.client = Client()
