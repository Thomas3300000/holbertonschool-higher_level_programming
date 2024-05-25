#!/usr/bin/env python3
"""Abstract Base Class"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        """ Abstract Method to make sound """
        pass


class Dog(Animal):
    def sound(self):
        """Method return the sound of the dog"""
        return "Bark"


class Cat(Animal):
    def sound(self):
        """Method return the sound of the cat"""
        return "Meow"
