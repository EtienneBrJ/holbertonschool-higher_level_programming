#!/usr/bin/python3
""" Module 5-rectangle"""


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
        """ Sets the width of a Rectangle instance."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Allows to find the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of a Rectangle instance."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return the area of a Rectangle instance."""
        return self.__height * self.__width

    def perimeter(self):
        """ Return the perimeter of a Rectangle instance."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ Prints a representation of a Rectangle instance
            if (height && width) != 0."""
        if self.__height == 0 or self.__width == 0:
            return ""
        square_rep = ""
        for i in range(self.__height):
            for j in range(self.__width):
                square_rep += '#'
            if i + 1 != self.__height:
                square_rep += '\n'
        return square_rep

    def __repr__(self):
        """ Prints a string representation of the rectangle to be able
            to recreate a new instance by using eval()"""
        return("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ Delete an instance"""
        print("Bye Rectangle...")
