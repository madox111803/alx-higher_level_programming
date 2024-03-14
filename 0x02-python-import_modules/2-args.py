#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys, argv) - 1
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else :
        print("{} arguments:".format(i))
    for num in range(1, i):
        print("{}: {}".format(i, sys.argv[i]))

