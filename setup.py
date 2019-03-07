from setuptools import setup

setup(
    name = 'py-cli-clock',
    version = '0.1.0',
    packages = ['py_clock'],
    entry_points = {
        'console_scripts': [
            'py_clock = py_clock.__main__:main'
        ]
    })
