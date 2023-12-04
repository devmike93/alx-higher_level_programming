#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i not in 'cC':
            new_string += i  # populate new string with everything
    return (new_string)     # that is not 'c' or 'C' in mystring
