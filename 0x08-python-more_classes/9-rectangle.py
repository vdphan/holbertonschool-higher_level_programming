#!/usr/bin/python3
"""Module to write an empty class Rectangle that defines a rectangle:
"""


class Rectangle:
    """This is an class Square that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                s += str(self.print_symbol) * self.__width + '\n'
        return s[:-1]

    def __repr__(self):
        """Called by the repr() built-in function"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
