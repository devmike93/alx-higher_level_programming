#!/usr/bin/python3
"""Module to define class BaseGeometry"""


class BaseGeometry:
    '''classe BaseGeometry'''

    def area(self):
        '''Area function'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates the input value'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
