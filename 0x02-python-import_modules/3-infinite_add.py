#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    inputs = argv[1:]
    output = 0
    for next_digit in inputs:
        output += int(next_digit)
    print("{:d}".format(output))
