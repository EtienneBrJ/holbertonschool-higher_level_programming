#!/usr/bin/python3
"""Unittest for Base class
"""
from models.base import Base
import unittest


class test_Base (unittest.TestCase):
    """Unittest class Base"""

    def test_baseId(self):
        """Unittest for base ID"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)
