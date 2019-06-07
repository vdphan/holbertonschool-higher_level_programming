#!/usr/bin/python3
def add_attribute(object, key, value):
    if not hasattr(object, "__dict__") and not hasattr(object, "__slots__"):
        raise TypeError("can't add new attribute")
    setattr(object, key, value)
