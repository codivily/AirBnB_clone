#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    __file_path = "file.json"
    __objects = dict() 

    def all(self):
        """Returns the dictionary __objects."""
        return (FileStorage.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (an object)
        """
        if obj.id in FileStorage.__objects:
            print("exists")
            return
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""
        obj_kwargs = [obj.to_dict() for key, obj in FileStorage.__objects.items()]

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_kwargs, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        only if the JSON file exists."""
        if not os.path.exists(FileStorage.__file_path):
            return

        obj_kwargs = []
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_kwargs = json.load(f)

        """ Reloading """
        for obj_kwarg in obj_kwargs:
            kclass = globals().get(obj_kwarg['__class__'])
            FileStorage.__objects[obj_kwarg['id']] = kclass(**obj_kwarg)
