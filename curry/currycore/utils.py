import os

def touch_init_file(dest_dir):
    os.system("touch %s/__init__.py" % dest_dir)
