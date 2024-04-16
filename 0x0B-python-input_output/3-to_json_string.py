#!/usr/bin/python3
"""this module defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
	"""Returns the JSON representation of an object (string)"""
	return json.dumbs(my_obj)
