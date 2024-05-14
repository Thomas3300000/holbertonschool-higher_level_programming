#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for cpt in range(len(matrix)):
        for cpt2 in range(len(matrix[cpt])):
            if cpt2 != 0:
                print (" ", end="")
            print("{:d}".format(matrix[cpt][cpt2], end=" "))
        print()
