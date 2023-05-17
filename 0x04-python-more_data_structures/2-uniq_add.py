#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list)).copy()
    sum = 0
    for i in new_list:
        print(i)
        sum =+ int(i)
    return sum
