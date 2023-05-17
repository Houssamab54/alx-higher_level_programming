#!/usr/bin/python3
def best_score(a_dictionary):
    l = []
    for i in a_dictionary:
        l.append(i)
    maximum = max(l)
    for i in a_dictionary.keys():
        if(a_dictionary[i] == maximum):
            return i
