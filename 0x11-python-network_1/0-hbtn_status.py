#!/usr/bin/python3
# a Python script that fetches https://intranet.hbtn.io/status
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    a = response.read()
    print("Body response:")
    print("    - type: {}".format(type(a)))
    print("    - content: {}".format(a))
    print("    - utf8 content: {}".format(a.decode("utf-8")))
