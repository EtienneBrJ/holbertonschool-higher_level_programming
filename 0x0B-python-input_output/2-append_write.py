#!/usr/bin/python3
""" Module append_write
"""


def append_write(filename="", text=""):
    """ Writes a string to a text file (UTF8)
        and returns the number of characters written.
    """
    with open(filename, 'a') as file:
        return file.write(text)
