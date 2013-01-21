"""
proofread.contrib.django_proofread.management.commands.proofread
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013 by Matt Robenolt
:license: BSD, see LICENSE for more details.
"""


from django.core.management.base import NoArgsCommand
from django.core.management import call_command


class Command(NoArgsCommand):
    help = 'Run the proofread endpoint tests'

    def handle_noargs(self, **options):
        call_command('test', 'django_proofread.ProofreadTestCase', **options)
