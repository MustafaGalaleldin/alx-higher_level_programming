#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ret = 0
    for i in range(len(roman_string)):
        if (i + 1 < len(roman_string) and
                rom[roman_string[i]] < rom[roman_string[i + 1]]):
            ret -= rom[roman_string[i]]
        else:
            ret += rom[roman_string[i]]

    return ret
