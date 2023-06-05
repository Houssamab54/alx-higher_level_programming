#!/usr/bin/python3
class Rectangle:
    """A class to represent a rectangle.

    Attributes:
        width (int): The width of the rectangle. Must be an integer greater than or equal to 0.
        height (int): The height of the rectangle. Must be an integer greater than or equal to 0.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.

    Example:
        >>> r = Rectangle(10, 20)
        >>> r.width
        10
        >>> r.height
        20
        >>> r.width = 30
        >>> r.width
        30
        >>> r.area()
        600
        >>> r.perimeter()
        80
    """

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class with optional width and height arguments."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
