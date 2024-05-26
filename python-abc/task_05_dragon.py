#!/usr/bin/env python3

class SwimMixin:
    def swim(self):
        """Define method swim"""
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        """Define method fly"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Define a class Dragon"""
    def roar(self):
        """Define method roar"""
        print("The dragon roars!")
