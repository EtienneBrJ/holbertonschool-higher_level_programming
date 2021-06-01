#!/usr/bin/python3
""" Module inherits_from"""


def inherits_from(obj, a_class):
    """ Return True if the object is an instance of a class
        that inherited from the specified class;
        otherwise False."""

    return issubclass(type(obj), a_class) if (type(obj) != a_class) else False
