#!/usr/bin/env python3

import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'py-cli-clock',
    version = '0.1.0',
    author = "Brian Matovu",
    author_email = "mtvbrianking@gmail.com",
    description = ("This is a demo project trying to learn Python basics; "
        "Project structure, documentation, automated tests, continous integration."),
    long_description = read('README.md'),
    license = "MIT",
    packages = ['py_clock'],
    keywords = "Python CLI Clock",
    url = "https://github.com/mtvbrianking/py-cli-clock",
    entry_points = {
        'console_scripts': [
            'py_clock = py_clock.__main__:main'
        ]
    })
