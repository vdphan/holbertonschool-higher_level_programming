#!/usr/bin/python3
"""
This module is to create a class that inherits from int.
"""


class MyInt(int):
    """a class that inherits from int"""
    def __ne__(self, other):
        """== and != operators inverted"""
        return super().__eq__(other)

    def __eq__(self, other):
        """== and != operators inverted"""
        return super().__ne__(other)
