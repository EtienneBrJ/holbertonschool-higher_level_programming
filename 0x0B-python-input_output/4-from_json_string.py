#!/usr/bin/python3
""" Module from_json_string
"""
import json


def from_json_string(my_obj):
    """ Returns an object (Python data structure) represented by a JSON string.
    """
    return json.loads(my_obj)
