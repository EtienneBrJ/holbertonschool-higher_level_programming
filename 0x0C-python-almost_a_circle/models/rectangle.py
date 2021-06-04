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

    