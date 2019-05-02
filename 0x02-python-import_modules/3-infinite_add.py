#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 0
    for i in range(len(argv)):
        if i != 0:
            a += int(argv[i])
    print(a)
