#!/usr/bin/python3
"""This module return  the dictionary description with simple data structure"""


def class_to_json(obj):
    """the dictionary description with simple data structure"""
    return obj.__dict__
