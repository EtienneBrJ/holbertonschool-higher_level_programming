#!/usr/bin/python3
"""Unittest for Base class
"""

import unittest
from models.base import Base


class TestBaseId(unittest.TestCase):
    """ Unitest for testing ID of Base class
    """
    def auto_assign_ID(self):
        b1 = Base()
        self.assertEqual(b1.id)

    def auto_assign_nextID(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b1.id +1)

    def save_passed_ID(self):
        b0 = Base()
        b1 = Base(89)
        self.assertEqual(b0.id + 89, b1.id)


if __name__ == "__main__":
    unittest.main()