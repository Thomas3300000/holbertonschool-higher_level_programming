#!/usr/bin/env python3

class CountedIterator:
    """Define a class CountedIterator"""
    def __init__(self, it):
        """Initialize counted iterator"""
        self.iterator = iter(it)
        self.count = 0

    def get_count(self):
        """Get count"""
        return self.count

    def __next__(self):
        """Get next item"""
        try:
            cpt = next(self.iterator)
            self.count += 1
            return cpt
        except StopIteration:
            raise StopIteration
