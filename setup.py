#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Xudoberdi G'ayratov
@contact: https://t.me/MrGayratov
@license MIT License, see LICENSE file

Copyright (C) 2024
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.0.6'

with open('README.md') as f:
    long_description = f.read()

setup(
    name='photolink',
    version=version,

    author="Xudoberdi G'ayratov",

    author_email='gayratov@xudoberdi.uz',
    url='https://github.com/xudoberdigayratov/PhotoLink',

    description='PhotoLink API wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',

    download_url='https://github.com/xudoberdigayratov/PhotoLink.git',
    license='MIT',

    packages=['photolink'],
    install_requires=['requests'],
    extras_require={
        'aio': ['httpx'],
    },

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)
