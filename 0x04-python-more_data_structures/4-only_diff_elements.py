#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = []
    for i in set_1:
        if not (i in set_2) and not (i in result):
            result.append(i)
    return result
