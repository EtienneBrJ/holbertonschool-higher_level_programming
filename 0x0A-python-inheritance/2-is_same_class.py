#!/usr/bin/python3
""" Module is_same_class."""


def is_same_class(obj, a_class):
    """ Returns True if the type of the object
        is exactly an instance of the specified class."""
    return True if type(obj) is a_class else False
