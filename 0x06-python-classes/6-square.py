#!/usr/bin/python3
""" Square Class."""


class Square:
    """
    Args:
        size (int): Size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Init the data."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """ Print in stdout the current square with #"""

        if self.__size == 0:
            print('')
        for i in range(self.__position[1]):
            print('')
        for j in range(self.__size):
            print(' ' * self.__position[0], end="")
            print('#' * self.__size)
