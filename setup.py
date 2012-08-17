#!/usr/bin/env python
from setuptools import setup, find_packages
 
setup(name='curry',
      author='toozoofoo',
      author_email='toozoofoo@gmail.com',
      description='',
      version='0.1',
      url='http://github.com/fay/curry',
      scripts=['bin/curry',],
      packages=find_packages(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Framework :: Django',
      ],
      include_package_data=True,
      zip_safe=False)
