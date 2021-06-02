#!/usr/bin/python3
""" Adding all arguments to a Python list
    and then saving them to a file.
"""


import sys
import json
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list_elem = []

if os.path.exists('add_item.json') and os.path.getsize('add_item.json') > 0:
    list_elem = load_from_json_file('add_item.json')

if len(sys.argv) > 1:
    for args in sys.argv[1:]:
        list_elem.append(args)

save_to_json_file(list_elem, 'add_item.json')
