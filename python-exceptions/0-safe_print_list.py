#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints up to x elements of a list safely using try/except.
    Returns the number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
