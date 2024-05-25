#!/usr/bin/python3
"""Create a class MyList that inherits from list"""


class MyList(list):
    """MyList that inherits from list"""

    def print_sorted(self):
        """Return a list sorted"""
        print(sorted(self))
