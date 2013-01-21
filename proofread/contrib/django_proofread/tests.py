"""
proofread.contrib.django_proofread.tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013 by Matt Robenolt
:license: BSD, see LICENSE for more details.
"""

from django.conf import settings
from django.test.client import Client
from django.core.handlers.wsgi import STATUS_CODE_TEXT
from proofread.base import BaseTestCase

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


class Endpoints(BaseTestCase):
    status_code_text = STATUS_CODE_TEXT
    endpoints = ENDPOINTS

    def setUp(self):
        self.client = Client()
