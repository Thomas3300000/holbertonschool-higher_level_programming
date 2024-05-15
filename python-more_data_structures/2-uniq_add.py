#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    number = 0

    for cpt in new:
        number += cpt
    return (number)
