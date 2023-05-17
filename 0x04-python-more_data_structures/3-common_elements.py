#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    for i in range(len(set_1)):
        for j in range(len(set_2)):
            result[i][j] = matrix[i][j] ** 2
    return result
