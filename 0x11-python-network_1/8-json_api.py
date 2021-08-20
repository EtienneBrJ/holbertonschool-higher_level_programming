#!/usr/bin/python3
""" Python script that takes in a letter
    and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    response = requests.post(url, data={'q': q})
    try:
        json_dict = response.json()
        if json_dict:
            print('[{}] {}'.format(json_dict['id'], json_dict['name']))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
