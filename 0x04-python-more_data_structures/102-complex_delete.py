#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    b = a_dictionary.copy()
    for k in b:
        if b[k] == value:
            del a_dictionary[k]
    return a_dictionary
