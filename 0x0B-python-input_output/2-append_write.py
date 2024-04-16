#!/usr/bin/python3
"""This module defines a text file-reading function"""


def write_file(filename="", text=""):
    """appends a string to a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
