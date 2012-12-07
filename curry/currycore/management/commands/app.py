from os import system, path
import sh

from django.core.management.base import BaseCommand, CommandError
from django.core.management.commands.startapp import Command as StartappCommand 

from django.conf import settings
from curry import currycore
from curry.currycore.commands import CurryCommand

class Command(CurryCommand, StartappCommand):

    def handle(self, app_name=None, target=None, **options):
        curry_dir = self.curry_dir()
        template = options.get('template', None)
        if not template:
            template = path.join(curry_dir, "templates/currycore/app_template")
            options['template'] = template
        super(Command, self).handle(app_name, target, **options)
        self.output("currycore/template_tag.py", path.join(app_name, "templatetags", app_name+ "_tags.py"))
