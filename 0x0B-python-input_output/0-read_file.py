#!/usr/bin/python3
""" Module read_file.
"""


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout"""
    with open(filename) as file:
        data = file.read()
        print(data, end='')
