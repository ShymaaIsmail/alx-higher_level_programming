#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv) - 1
    if args == 1:
        print("{:d} argument.".format(args))
    else:
        print("{:d} arguments.".format(args))
    for i in range(1, args):
        print("{}: {}".format(i, sys.argv[i]))
