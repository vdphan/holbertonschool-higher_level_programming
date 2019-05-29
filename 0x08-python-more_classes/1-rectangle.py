#!/usr/bin/python3
"""Module to write an empty class Rectangle that defines a rectangle:
"""


class Rectangle:
    """This is an class Square that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """function that retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set value for width """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """function that retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set value for height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
