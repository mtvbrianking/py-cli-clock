#!/usr/bin/env python3

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
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


# name = "an_example_pypi_project",
# version = "0.0.4",
# author = "Andrew Carter",
# author_email = "andrewjcarter@gmail.com",
# description = ("An demonstration of how to create, document, and publish "
#                                "to the cheese shop a5 pypi.org."),
# license = "BSD",
# keywords = "example documentation tutorial",
# url = "http://packages.python.org/an_example_pypi_project",
# packages=['an_example_pypi_project', 'tests'],
# long_description=read('README'),
# classifiers=[
#     "Development Status :: 3 - Alpha",
#     "Topic :: Utilities",
#     "License :: OSI Approved :: BSD License",
# ],
