#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_int_order(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_int_no_order(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_num(self):
        self.assertEqual(max_integer([1]), 1)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)

    if __name__ == '__main__':
        unittest.main()
