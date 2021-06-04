#!/usr/bin/python3
""" Module Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """ Class inheriting from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Private instance attributes (each with its own public getter and setter)
            Args:
                __width
                __height
                __x (position)
                __y (position)
                id
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieves the width attribute
        """
        return self.__width

    @property
    def height(self):
        """ Retrieves the height attribute
        """
        return self.__height

    @property
    def x(self):
        """ Retrieves the x attribute
        """
        return self.__x

    @property
    def y(self):
        """ Retrieves the y attribute
        """
        return self.__y

    @width.setter
    def width(self, value):
        """ Sets the width.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the height.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @x.setter
    def x(self, value):
        """ Sets the x.
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @y.setter
    def y(self, value):
        """ Sets the y.
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """ Public method:
            Returns the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """ Public method:
            Prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print('')

    