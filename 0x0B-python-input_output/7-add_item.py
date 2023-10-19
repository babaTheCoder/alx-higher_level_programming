#!/usr/bin/python3

"""adds all arguments to a python list and save as a file"""

import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

arguments = sys.argv[1:]
data = []

try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError as e:
    new_file = open("add_item.json", mode="w", encoding="utf-8")
    new_file.close()
finally:
    data.extend(arguments)
    save_to_json_file(data, "add_item.json")
