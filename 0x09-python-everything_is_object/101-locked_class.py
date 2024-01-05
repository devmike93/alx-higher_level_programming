#!/usr/bin/python3
"""Defines a locked Class"""


class LockedClass:
    """
    Prevent user from creating new instance attribute dynamically
    unless attribute is "first_name"
    """
    __slots__ = ("first_name",)
