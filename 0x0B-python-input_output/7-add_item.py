#!/usr/bin/python3
"""Add command-line arguments to a Python list and save them to a JSON file"""
from sys import argv


if __name__ == "__main__":
    save_json = __import__("5-save_to_json_file").save_to_json_file
    load_json = __import__("6-load_from_json_file").load_from_json_file

    # Check if the file exists and load its contents
    try:
        items = load_json("add_item.json")
    except FileNotFoundError:
        items = []

    # Add command-line arguments to the list
    for arg in argv[1:]:
        items.append(arg)

    # Save the updated list to the file
    save_json(items, "add_item.json")
