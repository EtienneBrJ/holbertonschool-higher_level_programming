#!/usr/bin/python3
"""
Module add-integer

Adds two integer together
"""


def add_integer(a, b=98):
    """ Return addition of a and b if they're integer or float.
    Raise Error if not
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)