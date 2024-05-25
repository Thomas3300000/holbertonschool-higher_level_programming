#!/usr/bin/python3
"""Create a function that returns True if the object is an instance 
otherwise False."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a class

    Args:
        obj: object
        a_class: class
    Returns:
        True if obj is an instance of a_class
        False if obj is not an instance of a_class
    """
    if type(obj) is not a_class:
        return False
    return True
