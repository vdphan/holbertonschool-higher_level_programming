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
        s = "[Rectangle] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width, self.height)
        return s
