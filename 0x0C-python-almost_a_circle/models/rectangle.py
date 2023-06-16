#!/usr/bin/python3
"""module of 'Rectangle' class"""

from .base import Base


class Rectangle(Base):
    """
    A class representing a rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """custom __str__ method for Rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x-coordinate attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y-coordinate attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate attribute.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

        def area(self):
            """
            Public method that returns the area of the rectangle.
            """
            return self.__width * self.__height
    
    def display(self):
        """
        Public method that prints the rectangle with the # character.
        """
        for i in range(self.__height):
            print("#" * self.__width)
