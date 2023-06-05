#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (number): The number to divide the matrix elements by.

    Returns:
        list of lists: The new matrix with the divided elements.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats or if div is not a number.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to zero.
        ValueError: If the matrix is empty.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not matrix:
        raise ValueError("matrix cannot be empty")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
