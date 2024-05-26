#!/usr/bin/env python3

class Fish:
    """Define a class Fish"""
    def swim(self):
        """Define method swim"""
        print("The fish is swimming")

    def habitat(self):
        """Define method habitat"""
        print("The fish lives in water")


class Bird:
    """Define a class Bird"""
    def fly(self):
        """Define method fly"""
        print("The bird is flying")

    def habitat(self):
        """Define method habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Define a class FlyingFish"""
    def fly(self):
        """Define method fly"""
        print("The flying fish is soaring!")

    def swim(self):
        """Define method swim"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Define method habitat"""
        print("The flying fish lives both in water and the sky!")
