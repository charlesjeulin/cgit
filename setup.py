#!usr/bin/env python3

from setuptools import setup

setup(
    name='cgit',
    version='1.0',
    packages=['cgit'],
    entry_points={
        'console_scripts': [
            'cgit=cgit.cli:main',
        ],
    },
)