#!/usr/bin/python3
# a Python script that fetches https://intranet.hbtn.io/status
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    a = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(a.decode("utf-8"))))
    print("\t- content: {}".format(a))
