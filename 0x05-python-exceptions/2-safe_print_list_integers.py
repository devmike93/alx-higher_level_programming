#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    arg_count = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            arg_count += 1
        except (TypeError, ValueError):
            continue
    print()
    return arg_count
