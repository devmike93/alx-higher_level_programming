#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    offset = 0 if (char - ord('a')) % 2 == 1 else 32
    print("{:c}".format(char - offset), end='')
