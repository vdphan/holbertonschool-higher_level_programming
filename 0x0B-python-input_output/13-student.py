#!/usr/bin/python3
"""
This module to create a class Student
"""


class Student:
    """class student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """retrieve public instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        e = {}
        d = self.__dict__
        if type(attrs) is list and all(isinstance(x, str) for x in attrs):
            for key, value in d.items():
                if key in attrs:
                    e[key] = value
            return e
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
