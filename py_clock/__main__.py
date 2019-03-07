"""
__main__.py
====================================
Entry file for py_clock package
"""

import argparse

def main():
    """
    This is the entry point for this file.

    :return:
    """
    parser = argparse.ArgumentParser(description="Simple CLI digital clock.")
    args = parser.parse_args()

if __name__ == '__main__':
    main()
