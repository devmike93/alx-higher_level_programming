#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    k = 0
    div_list = []
    while k < list_length:
        try:
            result = my_list_1[k] / my_list_2[k]
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            k += 1
            div_list.append(result)
    return div_list
