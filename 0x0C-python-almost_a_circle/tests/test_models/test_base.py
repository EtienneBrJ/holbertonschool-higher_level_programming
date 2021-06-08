#!/usr/bin/python3
"""Unittest for Base class
"""
from models.base import Base
import unittest


class test_Base (unittest.TestCase):
    """Unittest class Base"""

    def test_baseId(self):
        """Unittest for base ID
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(89)
        self.assertEqual(b4.id, 89)

    def test_to_json_string(self):
        """Unittest for all the JSON manipulation
        """
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, '[]')

        json_dictionary2 = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

        json_dictionary3 = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_dictionary3, '[{"id": 12}]')
        self.assertEqual(type(json_dictionary), str)
    
    def test_from_json_string(self):
        """Unittest for all the JSON manipulation
        """
        json_dict = Base.from_json_string(None)
        self.assertEqual(json_dict, [])

        json_dict2 = Base.from_json_string("[]")
        self.assertEqual(json_dict2, [])

        json_dict3 = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(json_dict3, [{"id": 89}])
        self.assertEqual(type(json_dict3), list)
    