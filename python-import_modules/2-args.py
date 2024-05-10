#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    cpt = len(sys.argv) - 1
    
    if cpt == 0:
        print("{} arguments.".format(cpt))
    elif cpt == 1:
        print("{} argument:".format(cpt))
    else:
        print("{} arguments:".format(cpt))

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))