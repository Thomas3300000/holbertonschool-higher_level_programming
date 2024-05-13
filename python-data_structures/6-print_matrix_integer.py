#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for cpt in matrix:
        for cpt2 in cpt:
            print("{}".format(cpt2), end=" ")
        print()
