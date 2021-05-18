#!/usr/bin/python3
""" Square Class."""


class Square:
    """
    Args:
        size (int): Size of the square
    """
    def __init__(self, size=0):
        """Init the data."""
        self._Square__size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self._Square__size

    @size.setter
    def size(self, value):
        """Set the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """ Return the current square area."""
        return self._Square__size ** 2

    def my_print(self):
        """ Print in stdout the current square with #"""
        if self._Square__size == 0:
            print('')
        for i in range(0, self._Square__size):
            for j in range(0, self._Square__size):
                print('#', end="")
            print('')
