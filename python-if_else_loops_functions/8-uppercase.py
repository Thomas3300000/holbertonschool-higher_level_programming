#!/usr/bin/python3
def uppercase(str):
    for cpt in (str):
        if ord(cpt) >= 97 and ord(cpt) <= 122:
            cpt = chr(ord(cpt) - 32)

        print("{}".format(cpt), end="")
    print("")
