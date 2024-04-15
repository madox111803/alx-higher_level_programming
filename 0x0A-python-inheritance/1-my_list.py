#!/usr/bin/python3
"""class mylist"""
class MyList(list):
    """prints sorted list of class"""
    def print_sorted(self):
        new = self [:]
        new.sort()
        print("{}".format(new))
