#!/usr/bin/python3
"""
This module to create a class Student"
"""
class Student:
    """class student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """retrieve public instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
