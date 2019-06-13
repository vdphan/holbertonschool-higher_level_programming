#!/usr/bin/python3
"""
Unittest all files and classes([..])
"""


import unittest
import io
import contextlib
import json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testbase(unittest.TestCase):
    def setUp(self):
        """set up nb_objects"""
        Base._Base__nb_objects = 0

    def test_id_is_not_None(self):
        """test if id is not None"""
        b1 = Base(2)
        b2 = Base(4)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 4)

    def test_id_is_None(self):
        """test if id is None"""
        b3 = Base()
        self.assertEqual(b3.id, 1)

        b4 = Base()
        self.assertEqual(b4.id, 2)

    def test_id_is_and_isnot_None(self):
        """test for mixed condition"""
        b5 = Base()
        self.assertEqual(b5.id, 1)

        b6 = Base(5)
        self.assertEqual(b6.id, 5)

    def test_id_is_Nan(self):
        """test for if id is nan"""
        b = Base(float("nan"))
        self.assertNotEqual(b.id, float("nan"))

    def test_id_is_not_integer(self):
        """test for id is not"""
        b7 = Base("hi")
        self.assertEqual(b7.id, "hi")

        b8 = Base(3.5)
        self.assertEqual(b8.id, 3.5)

        b9 = Base([])
        self.assertEqual(b9.id, [])

    def test_to_json_string_15(self):
        r1 = Rectangle(10, 7, 2, 8)
        d = r1.to_dictionary()
        j = Base.to_json_string([d])
        self.assertEqual(d,
                         {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertIs(type(d), dict)
        self.assertEqual([d], json.loads(j))

    def test_to_json_string_15_None(self):
        """test if dictionary is None"""
        d = Base.to_json_string([])
        self.assertEqual(d, "[]")

    def test_save_to_file(self):
        """test for function save to file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        a = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},
             {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(json.loads(f.read()), a)

    def test_save_to_file_None(self):
        """test if list objects is None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(json.loads(f.read()), [])

    def test_save_to_file_None(self):
        """test if list objects is None"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(json.loads(f.read()), [])

        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f1:
            self.assertEqual(json.loads(f1.read()), [])

    def test_save_tofile_Square(self):
        """test for Square"""
        Square.save_to_file(None)
        with open("Square.json", 'r') as f:
            self.assertEqual(json.loads(f.read()), [])

        Square.save_to_file([])
        with open("Square.json", 'r') as f1:
            self.assertEqual(json.loads(f1.read()), [])

        Square.save_to_file([Square(1)])
        a = [{'id': 1, 'size': 1, 'y': 0, 'x': 0}]
        with open("Square.json", 'r') as f2:
            self.assertEqual(json.loads(f2.read()), a)

    def test_save_tofile_Square1(self):
        a = [{'id': 1, 'size': 1, 'y': 0, 'x': 0}]
        Square.save_to_file([Square(1)])
        with open("Square.json", 'r') as f2:
            self.assertEqual(json.loads(f2.read()), a)

    def test_from_json_string(self):
        """test for function from_json_"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertEqual(list_output, list_input)

    def test_from_json_string_None(self):
        """test for json_string is None"""
        list_output = Rectangle.from_json_string(None)
        list_output2 = Rectangle.from_json_string([])

        self.assertEqual(list_output, [])
        self.assertEqual(list_output2, [])

    def test_create(self):
        """test for create function of rectangle"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_create_square(self):
        """test for create function of Square"""
        s1 = Square(1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(s2), "[Square] (1) 0/0 - 1")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_load_from_file(self):
        """test for load from file rectangle"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        lt = Rectangle.load_from_file()
        d = ["[Rectangle] (1) 2/8 - 10/7", "[Rectangle] (2) 0/0 - 2/4"]
        self.assertEqual(str(lt[0]), d[0])
        self.assertEqual(str(lt[1]), d[1])

    def test_load_from_file_square(self):
        """test for load from file square"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        ls = Square.load_from_file()
        d = ["[Square] (1) 0/0 - 5", "[Square] (2) 9/1 - 7"]
        self.assertEqual(str(ls[0]), d[0])
        self.assertEqual(str(ls[1]), d[1])

    if __name__ == '__main__':
        unittest.main()
