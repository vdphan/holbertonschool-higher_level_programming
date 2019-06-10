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
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """return an string"""
        s = "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args,  **kwargs):
        """assigns an argument to each attribute:"""
        for ele in args:
            if type(ele) is not int:
                raise TypeError("{} must be an integer".format(ele))
        att = ["id", "width", "height", "x", "y"]
        for idx in range(len(args)):
            for at in range(len(att)):
                if at == idx:
                    setattr(self, att[at], args[idx])
                    break

        if not args or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        d = dict()
        for key, value in self.__dict__.items():
            a = key.split("__")[-1]
            d[a] = value
        return d
