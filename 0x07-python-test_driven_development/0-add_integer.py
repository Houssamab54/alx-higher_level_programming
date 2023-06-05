#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats together and returns their sum as an integer.

    Parameters:
    a (int or float): The first number to be added.
    b (int or float): The second number to be added. Defaults to 98 if not provided.

    Raises:
    TypeError: If a or b is not an integer or a float.

    Returns:
    int: The sum of a and b, cast to an integer if necessary.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
