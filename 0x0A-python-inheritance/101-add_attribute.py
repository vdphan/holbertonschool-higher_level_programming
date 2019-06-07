#!/usr/bin/python3
"""
This module is to add attribute to object.
"""


def add_attribute(object, key, value):
    """function that add attribute"""
    if not hasattr(object, "__dict__") and not hasattr(object, "__slots__"):
        raise TypeError("can't add new attribute")
    if hasattr(object, "__slots__"):
        if key not in object.__slots__:
            raise TypeError("can't add new attribute")
    setattr(object, key, value)
