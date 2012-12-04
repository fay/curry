import sh
from os import system,path
from optparse import make_option


from django.core.management.base import AppCommand, BaseCommand, CommandError
from django.template.loader import render_to_string as render
from django.conf import settings

from curry import currycore
from curry.currycore.utils import touch_init_file

class Command(AppCommand):
    help = ''

    command_option = (make_option('-c', '--command-name',
                       action='store',
                       dest='command_name',
                       type='str',
                       help='command name'),)

    option_list = BaseCommand.option_list + command_option

    def handle(self, app, **options):
        command_name = options.get('command_name')
        CURRY_ROOT = path.abspath(path.dirname(currycore.__file__)) #: get curry core directory
        management_dir = path.join(app, "management") #: target project management directory
        commands_dir = path.join(management_dir, "commands") #: target project commands directory
        command_file = path.join(commands_dir, command_name + ".py") #: target project's command file
        if not path.isdir(commands_dir):
            system("mkdir -p %s" % (commands_dir))
            touch_init_file(management_dir)
            touch_init_file(commands_dir)
            print "[curry] create management template to %s" % (management_dir)
        
        if not path.exists(command_file):
            output = render("currycore/command.py")
            f = open(command_file, 'w')
            f.write(output)
            f.close()
