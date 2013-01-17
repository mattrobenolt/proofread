from django.core.management.base import NoArgsCommand
from django.core.management import call_command

class Command(NoArgsCommand):
    help = 'Run the proofread endpoint tests'

    def handle_noargs(self, **options):
        call_command('test', 'django_proofread.Endpoints')
