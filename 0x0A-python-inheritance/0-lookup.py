#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    # Get the list of attributes and methods of the object
    obj_dir = dir(obj)
    
    # Filter out any private attributes (i.e. those starting with '_')
    public_attrs = [attr for attr in obj_dir if not attr.startswith('_')]
    
    # Return the list of public attributes and methods
    return public_attrs
