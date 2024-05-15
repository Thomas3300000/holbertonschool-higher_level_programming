#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = sorted(a_dictionary)
    for cpt in order:
        print("{}: {}".format(cpt, a_dictionary[cpt]))
