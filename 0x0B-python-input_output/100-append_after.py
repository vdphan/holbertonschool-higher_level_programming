#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r',  encoding='utf-8') as f:
        a = f.readlines()
    for i in range(len(a)):
        if search_string in a[i]:
            a[i] = a[i] + new_string

    with open(filename, 'w',  encoding='utf-8') as f:
        for x in a:
            f.write(x)
