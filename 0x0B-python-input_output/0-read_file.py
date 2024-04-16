#!/usr/bin/python3
"""this module defines a text file-reading function"""


def read_file(filename=""):
	"""prints the content of a UTF8 text file"""
	with open(filename, encoding="utf-8") as f:
		print(f.read(), end='')
