#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        da = {"q": ""}
    elif len(sys.argv) == 2:
        da = {"q": sys.argv[1]}
    r = requests.post("http://0.0.0.0:5000/search_user", data=da)
    try:
        if json.loads(r.text) == {}:
            print("No result")
        else:
            print("[{}] {}".format(json.loads(r.text)['id'],
                                   json.loads(r.text)['name']))
    except ValueError:
            print("Not a valid JSON")
