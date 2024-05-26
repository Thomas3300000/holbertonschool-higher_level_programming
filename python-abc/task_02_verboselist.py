#!/usr/bin/env python3
from typing import Iterable


class VerboseList(list):
    """Class VerboseList"""
    
    def append(self, item):
        """Append an item to the list"""
        super().append(item)
        print("Added [{}] to the list".format(item))
        
    def extend(self, item):
        """Extend an item to the list"""
        super().extend(item)
        print("Extended the list with [{}] items".format(len(item)))
        
    def remove(self, item):
        """Remove an item from the list"""
        print("Removed [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list"""
        item = super().pop(index)
        print("Popped [{}] from the list".format(item))
        return item