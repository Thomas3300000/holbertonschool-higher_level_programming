#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    previous = 0

    for letters in roman_string:
        if letters not in roman:
            return (0)
        result += roman[letters]
        if roman[letters] > previous:
            result -= 2 * previous
        previous = roman[letters]
    return (result)
