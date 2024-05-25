#!/usr/bin/python3
"""Create a function that returns True if the object is an instance"""


def inherits_from(obj, a_class):
    """Check if an object is an instance or if object is an instance of
    a class that inherited from the specified class

    Args:
        obj: object
        a_class: class
    Returns:
        True if obj is an instance or if object is an instance of
        a_class
        False if obj is not an instance or if object is not an instance
        of a_class
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
