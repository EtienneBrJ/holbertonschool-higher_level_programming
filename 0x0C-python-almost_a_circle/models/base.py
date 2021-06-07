#!/usr/bin/python3
""" Module Base
"""
from os import path
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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of dicts to a file.
            Args:
                list_objs
                        A list of inherited Base instances.
        """
        file = cls.__name__ + ".json"
        list_dicts = []
        with open(file, "w") as json:
            if list_objs is None:
                json.write("[]")
            else:
                for elem in list_objs:
                    list_dicts.append(elem.to_dictionary())
                json.write(Base.to_json_string(list_dicts))
