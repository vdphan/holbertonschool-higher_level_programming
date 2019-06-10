#!/usr/bin/python3
"""
This module is to write the class Square that inherits from Rectangle:
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize size, x, y, id"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return an string"""
        s = "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)
        return s

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """set value for size"""
        self.width = value

    def update(self, *args, **kwargs):
        """function that  assigns attributes"""
        att = ["id", "size", "x", "y"]
        for idx, e in enumerate(args):
            setattr(self, att[idx], e)

        if not args and len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square:"""
        d = dict()
        for key, value in self.__dict__.items():
            a = key.split("__")[-1]
            if a == "width" or a == "height":
                d["size"] = value
            else:
                d[a] = value
        return d
