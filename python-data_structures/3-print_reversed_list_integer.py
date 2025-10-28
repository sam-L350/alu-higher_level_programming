#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order, one per line."""
    if my_list is None:
        return
    for num in my_list[::-1]:
        print("{:d}".format(num))
