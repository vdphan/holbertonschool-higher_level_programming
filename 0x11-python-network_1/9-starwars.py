#!/usr/bin/python3
""" a Python script that takes in a string and sends
a search request to the Star Wars API"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    r = requests.get(url, params={'search': sys.argv[1]})
    l = r.json()['results']
    s = ""
    for i in range(len(l)):
        if "name" in l[i]:
            s += l[i]['name'] + "\n"
    print("Number of results: {}".format(r.json()['count']))
    if r.json()['count'] > 0:
        print(s[:-1])
