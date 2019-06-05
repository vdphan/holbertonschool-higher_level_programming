#!/usr/bin/python3
"""
This module is to create a class that inherits from int.
"""


class MyInt(int):
    """a class that inherits from int"""
    def __ne__(self, other):
        """== and != operators inverted"""
        super().__eq__(self)
