#!/usr/bin/python3
"""Module to returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """function that returns the list of available attributes and methods"""
    return dir(obj)
