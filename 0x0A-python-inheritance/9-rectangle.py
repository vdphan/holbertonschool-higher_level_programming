#!/usr/bin/python3
"""This module is create an class that retrieve width and height"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that retrieve width and height"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def __str__(self):
        """return a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
