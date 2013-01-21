"""
proofread.base
~~~~~~~~~~~~~~

:copyright: (c) 2013 by Matt Robenolt
:license: BSD, see LICENSE for more details.
"""

import uuid
import unittest


def make_test(path, status, method='GET', data=None):
    """ Generate a test method """
    def run(self):
        response = getattr(self.client, method.lower())(path, data or {})
        self.assertEqual(response.status_code, status)
    return run


class BuildTestCase(type):
    def __new__(cls, name, bases, attrs):
        endpoints = attrs.get('endpoints', [])
        status_code_text = attrs.get('status_code_text', {})

        for path, status, method, data in endpoints:
            if not path.startswith('/'):
                path = '/' + path
            status_text = status_code_text.get(status, 'UNKNOWN')

            test = make_test(path, status, method, data)
            test.__name__ = name
            if data:
                test.__doc__ = '%s %s %r => %d %s' % (method, path, data, status, status_text)
            else:
                test.__doc__ = '%s %s => %d %s' % (method, path, status, status_text)

            test_name = 'test_proofread_%s' % uuid.uuid4().hex[:6]
            attrs[test_name] = test
        return super(BuildTestCase, cls).__new__(cls, name, bases, attrs)


class BaseTestCase(unittest.TestCase):
    __metaclass__ = BuildTestCase

    endpoints = ()
    status_code_text = {}
