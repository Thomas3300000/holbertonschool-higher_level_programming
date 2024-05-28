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

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student with specified attrs

        Args:
            attrs (list): List of attributes

        Returns:
            dict: Dictionary representation of a Student
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            dictionary = self.__dict__

            for cpt in attrs:
                if cpt in dictionary:
                    new_dict[cpt] = dictionary[cpt]
            return new_dict
