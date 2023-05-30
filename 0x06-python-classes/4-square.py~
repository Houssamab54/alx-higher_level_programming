#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        area(self): Returns the area of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (optional).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
