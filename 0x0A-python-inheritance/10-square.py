#!/usr/bin/python3
"""
This module creates a class Square that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle"""
    def __init__(self, size):
        """retrieve size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
