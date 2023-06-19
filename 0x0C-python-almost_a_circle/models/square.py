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

    def update(self, *args, **kwargs):
        """Updates the attributes of the squar"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """create dictionary representation of a square"""
        a_dict = {"id": 0, "size": 0, "x": 0, "y": 0}
        for key in a_dict:
            if key == "id":
                a_dict[key] = self.id
            elif key == "size":
                a_dict[key] = self.width
                a_dict[key] = self.height
            elif key == "x":
                a_dict[key] = self.x
            elif key == "y":
                a_dict[key] = self.y
        return a_dict
