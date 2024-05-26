#!/usr/bin/env python3
"""Abstract Base Class"""


from abc import ABC, abstractmethod
import math


class Shape (ABC):
    @abstractmethod
    def area(self):
        """ Abstract Method area """
        pass

    @abstractmethod
    def perimeter(self):
        """ Abstract Method perimeter """
        pass


class Rectangle (Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle"""
        return 2 * (self.width + self.height)


class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of circle"""
        return (math.pi * (self.radius * self.radius))

    def perimeter(self):
        """Return perimeter of circle"""
        return (math.pi * (self.radius * 2))


def shape_info(shape):
    """Print area and perimeter of shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
