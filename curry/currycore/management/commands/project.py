from os import system
from optparse import make_option

from django.core.management.base import AppCommand, BaseCommand, CommandError
from django.conf import settings
from django.core.management.commands.startproject import Command as StartProjectCommand 

from curry.currycore.commands import CurryCommand

class Command(CurryCommand, StartProjectCommand):

    def handle(self, project_name=None, target=None, *args, **options):
        curry_dir = self.curry_dir()
        template = options.get('template', None)
        if not template:
            template = "https://github.com/pinax/pinax-project-account/zipball/master"
            options['template'] = template
        super(Command, self).handle(project_name, target, **options)

