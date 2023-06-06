#!/usr/bin/python3
def copy_list(l):
    """
    Returns a copy of a list.

    This function creates a shallow copy of the input list using the slicing operator [:].
    A shallow copy creates a new list object with the same contents as the original list,
    but with a different memory address. If the original list contains mutable objects,
    the new list will still reference the same objects as the original list.

    Parameters:
    l (list): The list to be copied.

    Returns:
    list: A shallow copy of the input list.
    """
    return l[:]
