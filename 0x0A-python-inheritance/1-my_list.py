#!/usr/bin/python3
"""
===========================
this module comes with the class MyList
===========================
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """print a sorted list"""

        print(sorted(list(self)))
