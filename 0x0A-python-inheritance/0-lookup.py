#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """
    Return a list of attributes and methods associated with the given object.
    """
    return (dir(obj))
