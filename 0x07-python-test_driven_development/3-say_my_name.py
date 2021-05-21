#!/usr/bin/python3
"""
Add module say_my_name
Print: My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Add first_name and last_name to a string and print it
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = "My name is " + first_name + " " + last_name

    print("{}".format(full_name))
