#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle
"""superclass Rectangle"""

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """initialise inherited from rectangle"""
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """getter for size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
    
    def __str__(self):
        """string def"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)
