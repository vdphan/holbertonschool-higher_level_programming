#!/usr/bin/python3
# a Python script that fetches https://intranet.hbtn.io/status
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    a = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(a)))
    print("\t- content: {}".format(a))
    print("\t- utf8 content: {}".format(a.decode("utf-8")))
