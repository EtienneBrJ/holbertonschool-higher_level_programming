#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL and displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        response = requests.get(argv[1])
        print(response.text)
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(response.status_code))
