#!/usr/bin/python3
"""This module if the object is an instance of,
 or if the object is an instance of a class that inherited from,
the specified class """


def is_kind_of_class(obj, a_class):
    """check the class of instances"""
    return isinstance(obj, a_class)
