#!/usr/bin/python3
""" a Python script that takes in a string and sends a search
request to the Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    r = requests.get(url, params={'search': sys.argv[1]})
    data = r.json()
    l = r.json()['results']
    s = {}
    em = []
    for i in range(len(l)):
        for key, value in l[i].items():
            if key == "name" or key == "films":
                s[key] = value
        em.append(s)
        s = {}
    print("Number of results: {}".format(r.json()['count']))
    for ele in range(len(em)):
        print(em[ele]['name'])
        for link in em[ele]['films']:
            r1 = requests.get(link)
            print("\t{}".format(r1.json()['title']))
    while data['next'] is not None:
        r = requests.get(data['next'])
        data = r.json()
        l = data['results']
        s = {}
        em = []
        for i in range(len(l)):
            for key, value in l[i].items():
                if key == "name" or key == "films":
                    s[key] = value
            em.append(s)
            s = {}
        for ele in range(len(em)):
            print(em[ele]['name'])
            for link in em[ele]['films']:
                r1 = requests.get(link)
                print("\t{}".format(r1.json()['title']))
