#!/usr/bin/python3
"""Define serialization and deserialization XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize and save data in xml file

    Args:
        dictionary: data to save
        filename: name of the file
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize xml file and return data

    Args:
        filename: name of the file
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dic = {}
    for child in root:
        dic[child.tag] = child.text
    return dic
