#!/usr/bin/python3
""" Lists the last 10 commits
    of the repo and user passed in args
"""
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    name = argv[2]
    response = requests.get(url="http://api.github.com/repos/{}/{}/commits"
                                .format(name, repo), params={'per_page': 10},
                                headers={'Accept': 'application/vnd.github.v3+json'})
    json = response.json()
    for line in json:
        print("{}: {}".format(line.get("sha"),
                        line.get("commit").get("author").get("name")))