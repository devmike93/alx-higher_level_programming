#!/usr/bin/python3
"""Define a function that create object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
