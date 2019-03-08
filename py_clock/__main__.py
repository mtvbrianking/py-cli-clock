"""
__main__.py
====================================
Entry file for py_clock package
"""

from time import localtime, sleep, strftime
from sys import stdout
import argparse


def main():
    """
    This is the entry point for this file.

    :return:
    """

    # -----------------------------------------
    # Setup command meta
    # -----------------------------------------
    parser = argparse.ArgumentParser(description="Simple CLI digital clock.")
    args = parser.parse_args()

    # -----------------------------------------
    # Read current system time
    # -----------------------------------------

    datetime_str = localtime()

    time_str = strftime('%H:%M:%S', datetime_str)

    hours_str, minutes_str, seconds_str = time_str.split(':')

    hours = int(hours_str)
    minutes = int(minutes_str)
    seconds = int(seconds_str)

    # -----------------------------------------
    # Show clock
    # -----------------------------------------

    print("\nUse 'Ctrl+C' to quit.\n")

    while True:
        # print("%.2d:%.2d:%.2d" % (hours, minutes, seconds))
        stdout.write('\r%.2d:%.2d:%.2d' % (hours, minutes, seconds))
        stdout.flush()
        sleep(1)
        seconds += 1

        # Minutes
        if seconds == 60:
            minutes += 1
            seconds = 0

        # Hours
        if minutes == 60:
            hours += 1
            minutes = 0

        # Days
        if hours == 24:
            hours = 0


if __name__ == '__main__':
    main()
