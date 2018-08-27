#!/usr/bin/env python

from setuptools import setup

#with open("README", 'r') as f:
#    long_description = f.read()

setup(
   name='pypi_crawler',
   version='0.1',
   description='A small module to download packages from PyPi',
   license="MIT",
   long_description=long_description,
   author='Andreas Stamminger',
   author_email='andreas.stamminger@pm.me',
#   url="http://www.foopackage.com/",
   packages=['pypi_crawler'],
   install_requires=['requests', 'configparser'], 
)
