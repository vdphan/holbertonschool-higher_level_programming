#!/usr/bin/python3
def remove_char_at(str, n):
    a = ""
    for i, c in enumerate(str):
        if i != n:
            a = a + c
    return a
