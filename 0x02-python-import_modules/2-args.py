#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv) - 1
    if args == 1:
        print("{:d} argument:".format(args))
    elif args == 0:
        print("{:d} arguments.".format(args))
    else:
        print("{:d} arguments:".format(args))
    if args > 0:
        for i in range(1, args + 1):
            print("{}: {}".format(i, sys.argv[i]))
