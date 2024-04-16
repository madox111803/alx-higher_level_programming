#!/usr/bin/python3
""" this module defines a text file-reading function"""


def write_file(filename="", text=""):
	"""write a stringe to a UTF8 text file"""
	with open(filename, "w", encoding="utf-8") as f:
		return f.write(text) 
