#!/usr/bin/python3
"""Create class BaseGeometry"""


class BaseGeometry:
    """Define class BaseGeometry"""

    def area(self):
        """Define method area

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Define method integer_validator

        Args:
            name (str): The name of the parameter
            value (int): The value of the parameter
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
