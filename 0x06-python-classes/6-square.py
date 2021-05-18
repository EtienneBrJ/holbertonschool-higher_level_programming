#!/usr/bin/python3
""" Square Class."""


class Square:
    """
    Args:
        size (int): Size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Init the data."""
        self._Square__size = size
        self._Square__position = position

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

    @property
    def position(self):
        return self._Square__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value
