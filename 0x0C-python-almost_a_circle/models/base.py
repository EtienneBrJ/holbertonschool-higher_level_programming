#!/usr/bin/python3
""" Module Base
"""
import json


class Base:
    """ class Base with:
        Private class attribute: __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new instance of the Base class
            Args: id of the instance
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method:
            Returns the JSON string representation
            of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
