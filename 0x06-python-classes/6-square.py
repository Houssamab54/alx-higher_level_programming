#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of the square (private).

    Methods:
        area(self): Returns the area of the square.
        size(self): Gets the size of the square.
        size(self, value): Sets the size of the square.
        position(self): Gets the position of the square.
        position(self, value): Sets the position of the square.
        my_print(self): Prints the square with '#' characters.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (optional).
            position (tuple): The position of the square (optional).

        Raises:
            TypeError: If size is not is not a tuple of 2 positive integers.
            ValueError: If ess than 0 or position contains negative integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        return self.__size

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
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains negative integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
        or not all(isinstance(i, int) for i in value) \
        or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns thearea of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with '#' characters.

        Returns:
            None.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
