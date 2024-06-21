#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list = sorted(a_dictionary.keys())
    for key in list:
        print("{}: {}".format(key, a_dictionary[key]))
