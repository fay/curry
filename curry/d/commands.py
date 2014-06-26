import sh
from os import system,path
from optparse import make_option


from django.core.management.base import AppCommand, BaseCommand, CommandError
from django.template.loader import render_to_string as render
from django.conf import settings

from curry import d
from curry.d.utils import touch_init_file

class CurryCommand(BaseCommand):

    CURRY_ROOT = path.abspath(path.dirname(d.__file__)) #: get curry core directory

    def output(self, template_name, output_file):
        content = render(template_name)
        with open(output_file, 'w') as f:
            f.write(content)

    def curry_dir(self):
        return self.CURRY_ROOT
