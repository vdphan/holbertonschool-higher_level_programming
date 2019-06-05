#!/usr/bin/python3
"""Module to print sorted list:
"""


class MyList(list):
    """a class that inherits from list """
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
