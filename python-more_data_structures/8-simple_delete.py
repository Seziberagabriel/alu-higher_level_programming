#!/usr/bin/python3

def simple_delete(a_dictionary, key="")i:
    if a_dictionary:
        try:
           del a_dictionary[key]
        except KeyError:
           pass
        return a_dictionary
