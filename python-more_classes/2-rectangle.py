#!/usr/bin/python3
"""Create a class Rectangle"""


class Rectangle:
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)
