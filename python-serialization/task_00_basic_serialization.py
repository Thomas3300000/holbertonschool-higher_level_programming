#!/usr/bin/python3
"""Define Python module """
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data in json file
    
    Args:
        data: data to save
        filename: name of the file
    """
    with open(filename, "w") as f:
        json.dump(data, f)
    
def load_and_deserialize(filename):
    """Deserialize json file and return data
    
    Args:
        filename: name of the file
    """
    with open(filename, "r") as f:
        return json.load(f)
