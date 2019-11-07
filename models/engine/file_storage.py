#!/usr/bin/python3
"""Defines a FileStorage class."""
import json
from pathlib import Path


class FileStorage:
    """A class for object serialization using a JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Gets the __objects class attribute."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Deserializes the JSON file (__file_path) to __objects."""
        config = Path(FileStorage.__file_path)
        if config.is_file():
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
