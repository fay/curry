from os import system,path

from django.core.management.base import BaseCommand, CommandError

from settings import PROJECT_ROOT

class Command(BaseCommand):
    help = 'specify the cliparts images directory as args'

    """
    user_option = (make_option('-d', '--directory',
                       action='store',
                       dest='source_dir',
                       type='str',
                       help='specify the clipart directory'),)
    sys_option = (make_option('-f', '--file',
                       action='store',
                       dest='source_file',
                       type='str',
                       help='specify the clipart list file.'),)

    option_list = BaseCommand.option_list + user_option + sys_option
    """

    def handle(self,*args,**options):
        """
        parser = OptionParser(option_list=self.option_list)
        (options, args) = parser.parse_args()
        """
        app_name = args[0]
        CURRY_ROOT = path.join(PROJECT_ROOT,'curry') #path.abspath(path.dirname(__file__))
        system('cp -r %s/app_template %s' % (CURRY_ROOT,app_name))
