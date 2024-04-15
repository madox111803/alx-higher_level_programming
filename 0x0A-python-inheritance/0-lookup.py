#!/usr/bin/python3
"""Module implementing function to look up attributes of object"""
def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
