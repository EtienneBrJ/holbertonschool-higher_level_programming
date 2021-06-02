#!/usr/bin/python3
""" Module Student.
"""


class Student:
    """" class Student.
    """
    def __init__(self, first_name, last_name, age):
        """ Initialize a Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Public method
            Retrieves a dictionary representation of a Student instance.
        """
        dict = {}
        if attrs is None:
            return self.__dict__
        
        for i in attrs:
            if isinstance(i, str) and hasattr(self, i):
                dict[i] = getattr(self, i)
            else:
                pass

        return dict

    def reload_from_json(self, json):
        """ Public method
            replaces all attributes of the Student instance:
                You can assume json will always be a dictionary
                A dictionary key will be the public attribute name
                A dictionary value will be the value of the public attribute
        """
        for key in json.keys():
            self.__dict__[key] = json[key]
