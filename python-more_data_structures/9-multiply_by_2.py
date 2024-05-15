#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()

    for cpt in new:
        new[cpt] *= 2
    return (new)
