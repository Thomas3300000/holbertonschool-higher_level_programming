#!/usr/bin/python3
def uppercase(str):
    for cpt in (str):
        if ord(cpt) >= 97 and ord(cpt) <= 122:
            print("{}".format(chr(ord(cpt) - 32)), end="")
        else:
            print("{}".format(cpt), end="")
    print()
