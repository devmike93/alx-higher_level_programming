#!/usr/bin/python3
"""Define a class to JSON function"""


def class_to_json(obj):
    """
    Returns a dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object.
    """
    return obj.__dict__
