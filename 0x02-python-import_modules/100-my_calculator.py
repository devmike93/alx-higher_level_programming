#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operators = {'+': add, '-': sub, '*': mul, '/': div}
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if operator not in operators:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    result = operators[operator](a, b)
    print('{:d} {} {:d} = {:d}'.format(a, operator, b, result))
