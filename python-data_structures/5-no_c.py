#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for cpt in range(len(my_string)):
        if my_string[cpt] != 'c' and my_string[cpt] != 'C':
            str += my_string[cpt]
    return (str)
