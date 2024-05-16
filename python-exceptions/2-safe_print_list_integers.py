#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    result = 0

    for cpt in range(x):
        try:
            print("{:d}".format(my_list[cpt]), end="")
            result += 1
        except (TypeError, ValueError):
            continue
    print()
    return (result)
