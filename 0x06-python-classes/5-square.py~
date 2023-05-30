#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        area(self): Returns the area of the square.
        size(self): Gets the size of the square.
        size(self, value): Sets the size of the square.
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
        self.size = size

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("sizemust be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
