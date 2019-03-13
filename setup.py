#!/usr/bin/env python3

from setuptools import setup
from py_clock.utils import get_file_contents
from os import path

readme = path.abspath(path.join(path.dirname(__file__), "README.md"))

setup(
    name = 'py-cli-clock',
    version = '0.1.0',
    author = "Brian Matovu",
    author_email = "mtvbrianking@gmail.com",
    description = ("This is a demo project trying to learn Python basics; "
        "Project structure, documentation, automated tests, continuous integration."),
    long_description = get_file_contents(readme),
    license = "MIT",
    packages = ['py_clock'],
    keywords = "Python CLI Clock",
    url = "https://github.com/mtvbrianking/py-cli-clock",
    entry_points = {
        'console_scripts': [
            'py_clock = py_clock.__main__:main'
        ]
    })
