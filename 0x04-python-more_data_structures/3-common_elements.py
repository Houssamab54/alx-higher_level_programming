#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    for i in set_1:
        if (i in set_2) and not (i in result):
            result.append(i)
    return result
