# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fileStore',
    version='0.1.0',
    description='Python simple filestore and directory wrappers.',
    long_description=open('README.md').read(),
    author='Dean Haines',
    author_email='vbpupil@gmail.com',
    url='https://github.com/vbpupil/filestore',
    license=license,
    packages=['filestore', ],
)
