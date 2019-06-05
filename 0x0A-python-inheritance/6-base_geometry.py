#!/usr/bin/python3
"""This module is create an class with a function to raise error"""


class BaseGeometry:
    """A class that raise error"""
    def area(self):
        """function to raise error message"""
        raise Exception('area() is not implemented')
