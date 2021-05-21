#!/usr/bin/python3
"""
Add module print_square
Prints a square according to the size
"""

def print_square(size):
    """
    Prints a square according to the size in argument
    where the size is the lenght and width of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
