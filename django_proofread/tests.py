"""
django_proofread.tests
~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013 by Matt Robenolt
:license: BSD, see LICENSE for more details.
"""

import uuid
import unittest
from django.conf import settings
from django.test.client import Client
from django.core.handlers.wsgi import STATUS_CODE_TEXT


ENDPOINTS = []
for endpoint in getattr(settings, 'PROOFREAD_ENDPOINTS', []):
    if len(endpoint) < 4:
        endpoint = endpoint + ('', 200, 'GET', None)[len(endpoint):]
    ENDPOINTS.append(endpoint)

for key, status in (('SUCCESS', 200), ('FAILURES', 404)):
    for endpoint in getattr(settings, 'PROOFREAD_%s' % key, ()):
        ENDPOINTS.append((endpoint, status, 'GET', None))

if not ENDPOINTS:
    import warnings
    warnings.warn("You haven't specified any urls for Proofread to test!")


def make_test(path, status, method='GET', data=None):
    def run(self):
        response = getattr(self.client, method.lower())(path, data or {})
        self.assertEqual(response.status_code, status)
    return run


class BuildTestCase(type):
    def __new__(cls, name, bases, attrs):
        for path, status, method, data in ENDPOINTS:
            if not path.startswith('/'):
                path = '/' + path
            status_text = STATUS_CODE_TEXT.get(status, 'UNKNOWN')

            test = make_test(path, status, method, data)
            test.__name__ = name
            if data:
                test.__doc__ = '%s %s %r => %d %s' % (method, path, data, status, status_text)
            else:
                test.__doc__ = '%s %s => %d %s' % (method, path, status, status_text)

            test_name = 'test_proofread_%s' % uuid.uuid4().hex[:6]
            attrs[test_name] = test
        return super(BuildTestCase, cls).__new__(cls, name, bases, attrs)


class Endpoints(unittest.TestCase):
    __metaclass__ = BuildTestCase

    def setUp(self):
        self.client = Client()
