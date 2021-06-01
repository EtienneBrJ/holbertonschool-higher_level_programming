#!/usr/bin/python3
""" Module Square.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square inherit from Rectangle
    """
    def __init__(self, size):
        """ Initializes a square
            Instantion with size.
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns the area of a square instance.
            Overwrites the area() method of BaseGeometry)
        """
        return self.__size ** 2

    def __str__(self):
        """ Returns a string.
        """
        return str('[Square] {}/{}'.format(self.__size, self.__size))
