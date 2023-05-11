#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    sum = 0
    for i, arg in enumerate(arguments):
        sum = sum + int(arg)
    print("{:d}".format(sum))
