#!/usr/bin/python3
"""Create a function that adds 2 integers"""
    
    
def add_integer(a, b=98):
    """Returns sum of 2 integers (a and b)
    Args:
        a: first integer
        b: second integer
    Raises:
        TypeError: if a or b is not an integer
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
