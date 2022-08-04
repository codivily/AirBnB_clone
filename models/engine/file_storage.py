#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""

import json
import os
from models.base_model import BaseModel

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (an object)
        """
        key = "{}.{}".format(self.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""
        obj_dict = [obj.to_dict for obj in FileStorage.__objects.items()]

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        only if the JSON file exists."""
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)

        objects = [BaseModel(**params) for params in obj_dict]
        """Reloading"""
        FileStorage.__objects = {obj.id for obj in objects}
