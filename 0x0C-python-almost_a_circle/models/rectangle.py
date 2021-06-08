#!/usr/bin/python3
""" Module Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """ Class inheriting from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Private instance attributes
            (each with its own public getter and setter)
            Args:
                __width
                __height
                __x (position)
                __y (position)
                id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieves the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width.
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        """ Retrieves the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height.
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """ Retrieves the x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the x.
        """
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        """ Retrieves the y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the y.
        """
        if type(value) != int:
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

        for x in range(self.__y):
            print('')
        for i in range(self.__height):
            for y in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        """ Public method:
            assigns an argument to each attribute
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """ Public method:
            Returns the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ Return the print() and str() representation
            of the Rectangle.
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)