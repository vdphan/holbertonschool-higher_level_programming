#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for i in my_string:
        if i not in ['C', 'c']:
            s += i
    return s
