#!/usr/bin/python3
"""Module Mylist."""


class MyList(list):
    """class Mylist inherits from list."""

    def print_sorted(self):
        """ Public instance method
            Print an ascending sorted list."""
        print(sorted(self))
