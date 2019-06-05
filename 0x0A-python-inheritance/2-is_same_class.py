#!/usr/bin/python3
"""This module checka if the object is an instance of the specified class """


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of the specified class"""
    return type(obj) is a_class
