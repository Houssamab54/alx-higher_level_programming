#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Returns True if the given object is an exact instance of the specified class, False otherwise.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to check against.

    Returns:
    bool: True if obj is an exact instance of a_class, False otherwise.
    """
    return type(obj) is a_class
