#!/usr/bin/python3
"""Create class BaseGeometry"""


class BaseGeometry:
    """Define class BaseGeometry"""

    def area(self):
        """Define method area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Define method integer_validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Define class Rectangle"""

    def __init__(self, width, height):
        """Initialize rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
