#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            len(roman_string) == 0 or
            roman_string is None):
        return 0

    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    result = 0
    prev_value = 0

    for roman_char in roman_string[::-1]:
        if roman_dict.get(roman_char) is None:
            return 0
        current_value = roman_dict[roman_char]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        prev_value = current_value
    return result
