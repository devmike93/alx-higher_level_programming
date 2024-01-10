#!/usr/bin/python3
"""Define a Student Class"""


class Student:
    """Class represent a Student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a JSON
        dictionary.

        Args:
            json (dict): the key/values pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
