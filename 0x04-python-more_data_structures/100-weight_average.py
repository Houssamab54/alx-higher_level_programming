#!/usr/bin/python3
def weight_average(my_list=[]):
    result = [0, 0]
    for i in my_list:
        result[0] += i[0] * i[1]
        result[1] += i[1]
    result[0] = result[0] / result[1]
    return result[0]
