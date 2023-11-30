#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    inputs = argv[1:]
    argc = len(inputs)
    str_end = 's:' if argc > 1 else 's.' if argc == 0 else ':'
    print("{} argument{}".format(argc, str_end))
    for i, digit in enumerate(inputs, 1):
        print("{:d}: {}".format(i, digit))
