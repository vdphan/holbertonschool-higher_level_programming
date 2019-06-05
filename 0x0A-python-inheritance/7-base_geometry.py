#!/usr/bin/python3
"""This module is create an class with a function to raise error"""


class BaseGeometry:
    """A class that raise error"""
    def area(self):
        """function to raise area error message"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """function validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
