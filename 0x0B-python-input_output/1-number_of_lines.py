#!/usr/bin/python3
def number_of_lines(filename=""):
    c = 0
    with open(filename,  encoding='utf-8') as f:
        for line in f:
            c += 1
    return c
