#!/usr/bin/python3
"""Module to write an empty class Rectangle that defines a rectangle:
"""


class Rectangle:
    """This is an class Square that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.height = height
        self.width = width

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

    def area(self):
        """return rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Called by the str() built-in function"""
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(self.__height):
                s += '#' * self.__width + '\n'
        return s[:-1]

    def __repr__(self):
        """Called by the repr() built-in function"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
