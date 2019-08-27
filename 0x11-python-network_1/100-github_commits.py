#!/usr/bin/python3
""" a Python script that list 10 commits
(from the most recent to oldest) of the repository rails by the user rails
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.
                     format(sys.argv[1], sys.argv[2]))
    if len(r.json()) >= 10:
        for i in range(0, 10):
            print("{}: {}".format(r.json()[i]['sha'],
                                  r.json()[i]['commit']['author']['name']))
    else:
        for i in range(0, len(r.json())):
            print("{}: {}".format(r.json()[i]['sha'],
                                  r.json()[i]['commit']['author']['name']))
