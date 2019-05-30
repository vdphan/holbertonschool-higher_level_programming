#!/usr/bin/python3
def magic_string():
    magic_string.a = 0 if not hasattr(magic_string, 'a') else magic_string.a+1
    return("Holberton" + ", Holberton" * magic_string.a)
