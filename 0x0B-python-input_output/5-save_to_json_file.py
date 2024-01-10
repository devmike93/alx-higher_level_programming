#!/usr/bin/python3
"""Define a save object to a file function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a text file using its JSON representation.

    Args:
        my_obj: The object to be saved as JSON.
        filename (str): The name of the text file to save to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
