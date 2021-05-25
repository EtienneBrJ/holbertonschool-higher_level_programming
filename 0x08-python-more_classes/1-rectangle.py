#!/usr/bin/python3
""" Module 1-rectangle"""


class Rectangle:
    """ Define a Rectangle.
        Args:
            width of the rectangle
            height of the rectangle"""

    def __init__(self, width=0, height=0):
        """ Initialize a rectangle instance
            Args:
                height of a Rectangle
                width of a Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Allows to find the value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of a Rectangle instance.
            Args:
                width of a rectangle instance."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Allows to find the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of a Rectangle instance.
            Args:
                height of a rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
