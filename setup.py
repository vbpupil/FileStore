# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='file',
    version='0.1.0',
    description='Python simple file and directory wrappers.',
    long_description=readme,
    author='Dean Haines',
    author_email='vbpupil@gmail.com',
    url='https://github.com/vbpupil/file',
    license=license,
   packages=['file',],
)
