#!/usr/bin/python3
"""Define function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Function to save an object to a JSON file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
