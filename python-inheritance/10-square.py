#!/usr/bin/python3
"""Create class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define class Square"""

    def __init__(self, size):
        """Initialize square

        Args:
            size (int): The size of the new square
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return super().area()
