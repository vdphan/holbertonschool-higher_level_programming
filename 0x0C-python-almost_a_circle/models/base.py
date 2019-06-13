#!/usr/bin/python3
"""
This module is to create a class Base.
"""


import json
import os.path
import csv


class Base:
    """This class is the “base” of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """retrieve id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        name = cls.__name__ + ".json"
        with open(name, "w") as f:
            l = []
            if list_objs is not None:
                for obj in list_objs:
                    l.append(obj.to_dictionary())
                result = cls.to_json_string(l)
                f.write(result)
            else:
                f.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string:"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            value = cls(1, 1)
        if cls.__name__ == "Square":
            value = cls(1)
        value.update(**dictionary)

        return value

    @classmethod
    def load_from_file(cls):
        """function returns a list of instances"""
        fname = cls.__name__ + ".json"
        if not os.path.exists(fname):
            return []
        l = []
        with open(fname, "r") as f:
            output = cls.from_json_string(f.read())
            for ele in output:
                l.append(cls.create(**ele))
            return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        fname = cls.__name__ + ".csv"
        with open(fname, "w") as csvfile:
            c = csv.writer(csvfile)
            c.writerow(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        fname = cls.__name__ + ".csv"
        l = []
        with open(fname, "r") as f:
            d = csv.reader(f, delimiter=',')
            for row in d:
                for ele in row:
                    l.append(ele)
            return l
