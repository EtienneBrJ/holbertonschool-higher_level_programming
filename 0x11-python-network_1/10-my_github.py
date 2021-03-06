#!/usr/bin/python3
"""A Python script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get('https://api.github.com/user',
                            auth=(argv[1], argv[2]))
    json_dict = response.json()
    try:
        print(json_dict['id'])
    except KeyError:
        print('None')
