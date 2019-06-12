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


class test_rectangle(unittest.TestCase):
    def setUp(self):
        """set up nb_oject"""
        Base._Base__nb_objects = 0

    def test_with_no_error(self):
        """test with right output """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)


        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


    def test_with_width_getter_setter(self):
        """test getter and setter function"""
        r10 = Rectangle(10, 3)
        r10.width = 11
        self.assertEqual(r10.width, 11)

    def test_with_height_getter_setter(self):
        """test getter and setter function"""
        r = Rectangle(10, 4)
        r.height = 11
        self.assertEqual(r.height, 11)

    def test_with_x_getter_setter(self):
        """test getter and setter function"""
        r = Rectangle(10, 5)
        r.x = 11
        self.assertEqual(r.x, 11)

    def test_with_y_getter_setter(self):
        """test getter and setter function"""
        r = Rectangle(10, 6)
        r.y = 11
        self.assertEqual(r.y, 11)

    def test_with_height_error(self):
        """height error test"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r4 = Rectangle(10, -2)

    def test_with_width_error(self):
        """width error test"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r5 = Rectangle(3, 4)
            r5.width = -10

    def test_with_x_error(self):
        """x error test"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)


    def test_with_y_error(self):
        """y error test"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 2)
            r.y = "hi"

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 1, -10)

    def test_with_no_argument(self):
        """pass no argument to rectangle"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_with_area(self):
        """test function area"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_diplay_0(self):
        """test display function"""
        r1 = Rectangle(2, 3)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "##\n##\n##\n")


        r2 = Rectangle(2, 1)
        f1 = io.StringIO()
        with contextlib.redirect_stdout(f1):
            r2.display()
        self.assertEqual(f1.getvalue(), "##\n")

    def test_display_with_argument(self):
        """pass argument to display()"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 1)
            r2.display(1)

    def test_str(self):
        """check str funtion"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        f3 = io.StringIO()
        with contextlib.redirect_stdout(f3):
            print(r1)
        self.assertEqual(f3.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

        r2 = Rectangle(5, 5, 1)
        f4 = io.StringIO()
        with contextlib.redirect_stdout(f4):
            print(r2)
        self.assertEqual(f4.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")

        r3 = Rectangle(3, 2, 1, 1)
        self.assertEqual(str(r3), "[Rectangle] (2) 1/1 - 3/2")

    def test_display_with_xy(self):
        """pass x and y to display"""
        r1 = Rectangle(2, 3, 2, 2)
        f5 = io.StringIO()
        with contextlib.redirect_stdout(f5):
            r1.display()
        self.assertEqual(f5.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        r2 = Rectangle(3, 2, 1, 0)
        f6 = io.StringIO()
        with contextlib.redirect_stdout(f6):
            r2.display()
        self.assertEqual(f6.getvalue(), " ###\n ###\n")


    def test_update_0(self):
        """check update"""
        r1 = Rectangle(10, 10, 10, 10)
        f7 = io.StringIO()
        with contextlib.redirect_stdout(f7):
            print(r1)
        self.assertEqual(f7.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        f7 = io.StringIO()
        with contextlib.redirect_stdout(f7):
            print(r1)
        self.assertEqual(f7.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

        r2 = Rectangle(10, 10, 10, 10)
        r2.update(89, 2, 3, 4, 5)
        self.assertEqual(r2.id, 89)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)

    def test_update_0_error(self):
        """test error for update function"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(10, 10, 10, 10)
            r3.update(2, -2)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle(10, 10, 10, 10)
            r4.update(2, "2")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(2, 2, "2")

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(2, 2, -2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(2, 2, 2, 3, "5")

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(2, 2, 2, 3, -5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(2, 2, 2, "3")

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(2, 2, 2, -3)

    def test_update_1(self):
        """test for kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_1_args_not_empty(self):
        """test for kwargs if args is empty or doesn't exist"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_1_errors(self):
        """error tests for kwargs"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r3 = Rectangle(10, 10, 10, 10)
            r3.update(width=-1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle(10, 10, 10, 10)
            r4.update(width="2")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(height="2")

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(height=-2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(y="5")

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(y=-5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(x="3")

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(x=-3)

    def test_rectangle_to_dictionaries(self):
        """test for to dictionaries"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/9 - 10/2")
        r = r1.to_dictionary()
        self.assertEqual(r, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertIs(type(r), dict)

        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 1/1")
        r2.update(**r)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
        self.assertFalse(r1 == r2)


    if __name__ == '__main__':
        unittest.main()
