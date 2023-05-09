#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        result += chr(ord(c) - 32) if 'a' <= c <= 'z' else c
    print("{}".format(result), end="\n")
