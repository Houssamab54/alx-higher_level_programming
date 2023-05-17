#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary != None:
        l = []
        for i in a_dictionary.keys():
            l.append(a_dictionary[i])
        maximum = max(l)
        for i in a_dictionary.keys():
            if(a_dictionary[i] == maximum):
                return i
            else:
                return None
