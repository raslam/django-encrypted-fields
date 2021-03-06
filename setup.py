#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from setuptools import setup
import re
import sys

if sys.version_info[0]<3:
    raise RuntimeError("Python >=3 required.")


with open('encrypted_fields/__init__.py', 'r') as init_file:
    version = re.search(
        '^__version__ = [\'"]([^\'"]+)[\'"]',
        init_file.read(),
        re.MULTILINE,
    ).group(1)


setup(
    name='django-encrypted-fields-python3',
    description=(
        'This is a collection of Django Model Field classes '
        'that are encrypted using Keyczar.'
    ),
    url='http://github.com/defrex/django-encrypted-fields/',
    license='BSD',
    author='Aron Jones',
    author_email='aron.jones@gmail.com',
    packages=['encrypted_fields'],
    version=version,
    install_requires=[
        'Django>=1.4',
        'python3-keyczar>=0.71c',
    ],
)
