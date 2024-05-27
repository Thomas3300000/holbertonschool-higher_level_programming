#!/usr/bin/python3
"""Define function from_json_string"""
import json


def from_json_string(my_obj):
    """Returns an object represented by a JSON string"""
    return json.loads(my_obj)
