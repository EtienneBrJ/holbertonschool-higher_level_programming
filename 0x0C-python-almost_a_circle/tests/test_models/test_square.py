#!/usr/bin/python3
"""Unittest for Rectangle class
"""
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest


class test_Square (unittest.TestCase):
    """Unittest class Square
    """
    def test_rect(self):
        """Unittest:
            Does Square exist?
        """
        with self.assertRaises(TypeError):
            r5 = Square("1", 2)
        try:
            r5 = Square("1", 2)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        with self.assertRaises(TypeError):
            r5 = Square(1, "2")
        try:
            r5 = Square(1, "2")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer")

        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 2)
        try:
            r5 = Rectangle(0, 2)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "width must be > 0")
            
        with self.assertRaises(ValueError):
            r5 = Rectangle(2, 0)
        try:
            r5 = Rectangle(2, 0)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "height must be > 0")

        with self.assertRaises(TypeError):
            r5 = Square(1, 2, "3", 4)
        try:
            r5 = Square(1, 2, "3", 4)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer")


        with self.assertRaises(ValueError):
            r5 = Square(1, 2, -1, 3)
        try:
            r5 = Square(1, 2, -1, 3)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "y must be >= 0")

        self.assertEqual(7, Square(10, 2, 0, 7).id)

        r_area = Square(1, 2).area()
        self.assertEqual(r_area, 1)

        r_str = Square(1, 1, 1, 1)
        self.assertEqual(str(r_str), '[Square] (1) 1/1 - 1')

        
    



        

