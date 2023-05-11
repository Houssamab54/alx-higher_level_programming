#!/usr/bin/python3                                                              
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]                                
    num_arguments = len(arguments)
    print("{:d} argument".format(num_arguments), end='')
    if num_arguments > 0:
        if num_arguments == 1:
            print(":")
        else:
            print("s:")
        for i, arg in enumerate(arguments):
            print("{}: {}".format(i+1, arg))
    else:
        print("s.")
