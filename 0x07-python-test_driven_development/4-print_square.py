#!/usr/bin/python3

def print_square(size):
    """
    Prints a square made up of "#" characters with each side of the square being `size` characters long.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than zero.

    Returns:
        None
    """

    # Check if `size` is a valid integer value
    if type(size) is not int:
        raise TypeError("size must be an integer")

    # Check if `size` is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if `size` is a valid integer value, even if it is negative
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    # Print the square
    for i in range(size):
        print("#" * size)
