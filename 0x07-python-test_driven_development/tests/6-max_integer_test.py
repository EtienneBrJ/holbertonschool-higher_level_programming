#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):

    def test_regular(self):
        """ Test with a regular list of ints: should return the max result"""
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """Test with a list of non-ints and ints:
        should raise a TypeError exception"""
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        """Test with an empty list: should return None"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative values: should return the max"""
        l = [-2, -3, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        l = [1, 5.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 5.5)

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 1)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        l = [5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        l = [1, 1, 1, 1, 1]
        result = max_integer(l)
        self.assertEqual(result, 1)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        l = ["Holberton", "School"]
        result = max_integer(l)
        self.assertEqual(result, "Holberton")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()