#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for cpt in range(len(matrix)):
        for cpt2 in range(len(matrix[cpt])):
            print("{:d}".format(matrix[cpt][cpt2]), end="")
            if cpt2 != (len(matrix[cpt]) - 1):
                print(" ", end="")
        print()
