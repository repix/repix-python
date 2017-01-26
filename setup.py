#!/usr/bin/env python
# coding=utf-8
from distutils.core import setup

setup(
    name='repix',
    version='0.1.0',
    author='repix.io',
    author_email='dev@repix.io',
    packages=['repix'],
    scripts=[],
    url='https://www.repix.io',
    license='LICENSE',
    description='Python client for repix.io',
    long_description=open('README.rst').read(),
    install_requires=['imboclient==0.1.2', 'pytest', ]
)

