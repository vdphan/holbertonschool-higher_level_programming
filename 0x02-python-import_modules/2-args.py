#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{} arguments".format(len(argv) - 1), end="")
    if len(argv) > 1:
        print(":")
    else:
        print(".")
    for i in range(len(argv)):
        if i != 0:
            print("{}: {}".format(i, argv[i]))
