#!/usr/bin/python3
"""
This module is to create a class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize width, height, x, y, id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """function that retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set value for width """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
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
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """function that retrieve height"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter to set value for height"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """function that retrieve height"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter to set value for height"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """return rectangle area"""
        return self.__height * self.__width

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__height):
            print("#" * self.__width)
