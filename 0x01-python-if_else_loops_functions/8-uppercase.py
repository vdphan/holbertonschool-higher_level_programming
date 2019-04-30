#!/usr/bin/python3
def uppercase(str):
    for c in str:
        a = ord(c)
        if (ord(c) < 123 and ord(c) > 96):
            a = a - 32
        print("{}".format(chr(a)), end="")
    print("")
