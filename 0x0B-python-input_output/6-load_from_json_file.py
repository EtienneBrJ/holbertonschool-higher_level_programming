#!/usr/bin/python3
""" Module load_from_json_file
"""
import json


def load_from_json_file(filename):
    """ Creates an Object from a “JSON file”
    """
    with open(filename) as file:
        return json.load(file)
