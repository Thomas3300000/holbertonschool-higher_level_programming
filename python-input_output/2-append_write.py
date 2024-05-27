#!/usr/bin/python3
"""Define function append_write"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file
    and returns the number of characters
    
    Args:
        filename: name of file
        text: text to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
