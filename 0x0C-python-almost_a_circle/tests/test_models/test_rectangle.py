#!/usr/bin/python3
"""Unittest for Rectangle class
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest


class test_Rectangle (unittest.TestCase):
    """Unittest class Rectangle
    """
    def test_rect(self):
        """Unittest:
            Does Rectangle exist?
        """
        with self.assertRaises(TypeError):
            r5 = Rectangle("1", 2)
        try:
            r5 = Rectangle("1", 2)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "width must be an integer")

        with self.assertRaises(TypeError):
            r5 = Rectangle(1, "2")
        try:
            r5 = Rectangle(1, "2")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "height must be an integer")

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
            r5 = Rectangle(1, 2, "3", 4)
        try:
            r5 = Rectangle(1, 2, "3", 4)
        except TypeError as exception:
            self.assertEqual(exception.args[0], "x must be an integer")

        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 2, 3, "4")
        try:
            r5 = Rectangle(1, 2, 3, "4")
        except TypeError as exception:
            self.assertEqual(exception.args[0], "y must be an integer")

        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 2, 3, -3)
        try:
            r5 = Rectangle(1, 2, 3, -3)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "y must be >= 0")

        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 2, -1, 3)
        try:
            r5 = Rectangle(1, 2, -1, 3)
        except ValueError as exception:
            self.assertEqual(exception.args[0], "x must be >= 0")

        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

        r_area = Rectangle(1, 2).area()
        self.assertEqual(r_area, 2)

        r_str = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(str(r_str), '[Rectangle] (1) 1/1 - 1/1')


    def test_to_json_string_rec(self):
        """Unittest for all the JSON manipulation
        """
        json_dictionary = Rectangle.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')

        json_dictionary2 = Rectangle.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

        json_dictionary3 = Rectangle.to_json_string([{'id': 12}])
        self.assertEqual(json_dictionary3, '[{"id": 12}]')
        self.assertEqual(type(json_dictionary), str)
    
    def test_from_json_string_rec(self):
        """Unittest for all the JSON manipulation
        """
        json_dict = Rectangle.from_json_string(None)
        self.assertEqual(json_dict, [])

        json_dict2 = Rectangle.from_json_string("[]")
        self.assertEqual(json_dict2, [])

        json_dict3 = Rectangle.from_json_string('[{ "id": 89 }]')
        self.assertEqual(json_dict3, [{"id": 89}])
        self.assertEqual(type(json_dict3), list)
    



        

