#!/usr/bin/python3
"""Create class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define class Rectangle"""

    def __init__(self, width, height):
        """Initialize rectangle

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        self.__height = height
        self.__width = width
        self.integer_validator("width", width)
        self.integer_validator("height", height)
