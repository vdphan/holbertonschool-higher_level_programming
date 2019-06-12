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


class testbase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_is_not_None(self):
        b1 = Base(2)
        b2 = Base(4)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 4)

    def test_id_is_None(self):
        b3 = Base()
        self.assertEqual(b3.id, 1)

        b4 = Base()
        self.assertEqual(b4.id, 2)

    def test_id_is_and_isnot_None(self):
        b5 = Base()
        self.assertEqual(b5.id, 1)

        b6 = Base(5)
        self.assertEqual(b6.id, 5)

    def test_id_is_Nan(self):
        b = Base(float("nan"))
        self.assertNotEqual(b.id, float("nan"))

    def test_id_is_not_integer(self):
        b7 = Base("hi")
        self.assertEqual(b7.id, "hi")

        b8 = Base(3.5)
        self.assertEqual(b8.id, 3.5)

        b9 = Base([])
        self.assertEqual(b9.id, [])



    if __name__ == '__main__':
        unittest.main()
