#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import sys


if __name__ == "__main__":
    value = {"Your email is": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        b = response.read()
        print(b.decode("utf-8"))
