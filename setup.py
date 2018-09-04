#!/usr/bin/env python

from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='pypi_downloader',
   version='1.0',
   description='A small utility to download packages from PyPi',
   license="MIT",
   long_description=long_description,
   author='Andreas Stamminger',
   author_email='andreas.stamminger@pm.me',
   scripts=['bin/sync_package_cache'],
   url="https://github.com/astamminger/pypi_downloader",
   packages=['pypi_downloader'],
   install_requires=['requests', 'click', 'configparser'], 
)
