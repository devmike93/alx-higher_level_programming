#!/usr/bin/python3
"""
Reads lines from standard input, calculates file size and status code counts,
and prints statistics every 10 lines.
"""


def print_stats(size, status_codes):
    """
    Print the file size and status codes in a sorted order.

    Args:
        size (int): The file size.
        status_codes (dict): A dictionary containing status codes and their
                             counts.
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")


if __name__ == "__main__":
    import sys
    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            try:
                split_line = line.split()
                size += int(split_line[-1])

                if split_line[-2] in valid_codes:
                    status_codes[split_line[-2]] = (
                            status_codes.get(split_line[-2], 0) + 1)
            except (IndexError, ValueError):
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
