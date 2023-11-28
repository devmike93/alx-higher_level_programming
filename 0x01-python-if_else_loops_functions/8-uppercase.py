#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        result += upper_char
    print("{}".format(result))
