#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError('text must be a string')
    s = ""
    for i in text:
        s += i
        if i == '.' or i == '?' or i == ':':
            print(s.strip())
            print()
            s = ""
    print(s.strip(), end="")
