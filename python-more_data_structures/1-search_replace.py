#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for cpt in range(len(new)):
        if new[cpt] == search:
            new[cpt] = replace
    return (new)
