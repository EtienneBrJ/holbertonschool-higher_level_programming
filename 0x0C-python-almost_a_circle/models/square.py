#!/usr/bin/python3
""" Module Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize an instance square from the class Rectangle.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieves the size of the square.
        """
        return self.width

    @size.setter
    def size(self, size):
        """ Sets the size of the Square.
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Public method:
            assigns an argument to each attribute
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == 'size':
                    self.width = v
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
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ Return the print() and str() representation
            of the Square.
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)
