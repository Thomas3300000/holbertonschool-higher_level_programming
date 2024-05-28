#!/usr/bin/python3
"""Define a class Student."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize a Student

        Args:
            first_name (str): First name
            last_name (str): Last name
            age (int): Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return the dictionary representation of a Student"""
        return self.__dict__
