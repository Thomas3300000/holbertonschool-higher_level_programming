#!/usr/bin/python3
def fizzbuzz():
    for cpt in range(1, 101):
        if cpt % 3 == 0 and cpt % 5 == 0:
            print("FizzBuzz", end=" ")
        elif cpt % 3 == 0:
            print("Fizz", end=" ")
        elif cpt % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(cpt), end=" ")
