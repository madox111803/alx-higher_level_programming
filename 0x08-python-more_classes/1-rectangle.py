#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""
class Rectangle:
    """Rectangle class defined by width and height"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance"""
        self.width = width
        self.height = height
    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.width = value
    @property
    def height(self):
        """Retrieves the width of a Rectangle instance"""
        return self.__height
    @height.setter
    def height(self, value):
        """Sets the width of a Rectangle instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
