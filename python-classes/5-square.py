#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): The size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""

        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for cpt in range(self.__size):
                for cpt2 in range(self.__size):
                    print("#", end="")
                print()
