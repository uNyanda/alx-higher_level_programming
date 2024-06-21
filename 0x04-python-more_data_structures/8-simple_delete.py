#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    exist = a_dictionary.get(key)

    if exist:
        del a_dictionary[key]

    return a_dictionary
