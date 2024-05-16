#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for cpt in range(list_length):
        try:
            result = my_list_1[cpt] / my_list_2[cpt]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new.append(result)
    return (new)
