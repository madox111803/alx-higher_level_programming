#!/usr/bin/python3
"""Area of a square"""


class Square:
    """Private instance attribute: size
    Instantiation with area method """

    def __init__(self, size=0):
        """init attribute size"""
        self.__size = size
    
    @property
    """getter/setter for square"""
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """init attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an interger")
        elif value < 0:
            raise ValueError("size must be an interger")
        else:
            self.__size = value
    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)

