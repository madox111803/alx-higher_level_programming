#!/usr/bin/python3
def max_integer(my_list=[]):
    lenght = len(my_list)
    if lenght == 0:
        return None
    maxint = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > maxint:
            maxint = my_list[i]
        return maxint
