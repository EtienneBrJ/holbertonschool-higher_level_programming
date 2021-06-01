#!/usr/bin/python3
""" Module BaseGeometry.
"""


class BaseGeometry:
    """ class BaseGeometry.
    """
    pass

    def area(self):
        """ Add tests.
        """
        try:
            self.area()
        except:
            raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Public instance method:
            that validate value

            Args:
                Name (assume that is always a string)
                Value
                    Raise errors exception if not int or <= 0
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
