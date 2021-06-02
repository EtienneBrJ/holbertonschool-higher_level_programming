#!/usr/bin/python3
""" Adding all arguments to a Python list
    and then saving them to a file.
"""


from sys import argv
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    list_elem = load_from_json_file("add_item.json")
except:
    list_elem = []

for args in (argv[1:]):
    list_elem.append(args)

save_to_json_file(list_elem, "add_item.json")
