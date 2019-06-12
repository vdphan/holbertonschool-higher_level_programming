#!/usr/bin/python3
"""
Unittest all files and classes([..])
"""


import unittest
import io
import contextlib


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_square(unittest.TestCase):
    def setUp(self):
        """set up nb_oject"""
        Base._Base__nb_objects = 0

    def test_square_init_10(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s1.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n#####\n#####\n#####\n")


        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        f1 = io.StringIO()
        with contextlib.redirect_stdout(f1):
            s2.display()
        self.assertEqual(f1.getvalue(), "  ##\n  ##\n")

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        f2 = io.StringIO()
        with contextlib.redirect_stdout(f2):
            s3.display()
        self.assertEqual(f2.getvalue(), "\n\n\n ###\n ###\n ###\n")


    def test_square_10_instance(self):
        """test with instance"""
        s1 = Square(10, 2)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 10)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.x, 10)
        self.assertEqual(s2.y, 0)


        s3 = Square(2, 0, 0, 12)
        self.assertEqual(s3.id, 12)

    def test_square_11_getter_setter(self):
        """test square size getter and setter"""
        s = Square(10, 3)
        self.assertEqual(s.size, 10)
        s.size = 2
        self.assertEqual(s.size, 2)


        s2 = Square(5)
        self.assertEqual(str(s2), "[Square] (2) 0/0 - 5")
        s2.size = 10
        self.assertEqual(s2.size, 10)

    def test_square_11_error(self):
        """test for raising errors"""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "2"

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -2

    def test_square_update_12(self):
        """test for square update"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_square_update_12_error_and_skip(self):
        """test for udapte error and skip condition"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s3 = Square(10, 10, 10, 10)
            s3.update(2, -2)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s4 = Square(10, 10, 10, 10)
            s4.update(2, "2")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s5 = Square(10, 10, 10, 10)
            s5.update(2, 2, 2, "5")

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s5 = Square(10, 10, 10, 10)
            s5.update(2, 2, 3, -5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s5 = Square(10, 10, 10, 10)
            s5.update(2, 2, "3")

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s5 = Square(10, 10, 10, 10)
            s5.update(2, 2, -3)

    def test_to_dictionary_square(self):
        """to dictionary test"""
        s1 = Square(10, 2, 1)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertIs(type(s1_dictionary), dict)

        s2 = Square(1, 1)
        self.assertEqual(str(s2), "[Square] (2) 1/0 - 1")
        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertFalse(s1 == s2)
