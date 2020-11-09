#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="csv-stripper",
    version="1.0",
    py_modules=['stripper'],
    install_requires=[
        'click'
    ],
    entry_points= '''
        [console_scripts]
        stripper=stripper:cli
    ''',
)
