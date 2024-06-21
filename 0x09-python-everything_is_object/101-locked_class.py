#!/usr/bin/python3
"""
This module defines a class LockedClass.
There are no object attributes.
"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called
    first_name.
    """
    def __setattr__(self, name, value):
        if name != 'first_name' and name != '__dict__':
            raise AttributeError("'{}' object has no attribute \
'{}'".format(self.__class__.__name__, name))
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        if name == '__dict__':
            raise AttributeError("'{}' object has no \
attribute '{}'".format(self.__class__.__name__, name))
        return super().__getattribute__(name)
