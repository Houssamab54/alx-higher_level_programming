#!/usr/bin/python3
class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0): Initializes a new instance of the Rectangle class.
        area(self): Returns the area of the rectangle.
        perimeter(self): Returns the perimeter of the rectangle.
        __str__(self): Returns a string representation of the rectangle.

    Raises:
        TypeError: If the width or height is not an integer.
        ValueError: If the width or height is less than 0.

    Usage:
        rectangle = Rectangle(3, 4)
        print(rectangle.area()) # Output: 12
        print(rectangle.perimeter()) # Output: 14
        print(rectangle) # Output: 
                         # ###
                         # ###
                         # ###
                         # ###
        rectangle.width = 5
        rectangle.height = 2
        print(rectangle.area()) # Output: 10
        print(rectangle.perimeter()) # Output: 14
        print(rectangle) # Output: 
                         # #####
                         # #####
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than 0.
        """

        self.width = width
        self.height = height
    
    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """

        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
        
    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """

        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
        
    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.width * self.height
    
    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.

        Notes:
            If the width or height is equal to 0, the perimeter will be equal to 0.
        """

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2
    
    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.

        Notes:
            If the width or height is equal to 0, an empty str.
        """

        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.height):
                rectangle += "#" * self.width
                if i != self.height - 1:
                    rectangle += "\n"
            return rectangle
