#!/usr/bin/python3
"""the 'Base' class"""

import json


class Base:
    """definition  of Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
