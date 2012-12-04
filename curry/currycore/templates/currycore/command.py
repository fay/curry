from optparse import make_option

from django.core.management.base import AppCommand, BaseCommand, CommandError
from django.conf import settings

class Command(AppCommand):
    help = ''

    command_option = (make_option('-o', '--your-option',
                       action='store',
                       dest='your_option',
                       type='str',
                       help=''),)

    option_list = BaseCommand.option_list + command_option

    def handle(self, app, **options):
        pass

