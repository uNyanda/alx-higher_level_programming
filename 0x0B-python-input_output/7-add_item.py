#!/usr/bin/python3
"""
This module contains a script that adds all arguments to a Python list, and
then saves them to a file.
"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

for item in sys.argv[1:]:
    my_list.append(item)

save_to_json_file(my_list, filename)
