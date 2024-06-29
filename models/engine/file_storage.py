#!/usr/bin/python3

"""
This script contains the file storage which serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import os
import json
from models.base_model import BaseModel

class FileStorage:
    """
    Represents the file storage for the project.
    """
    __file_path = "file.json"
    __objects = {}
    CLASSES = {
        "BaseModel": BaseModel
    }

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {key: obj.to_dict() for key, obj in FileStorage.__objects.items()},
                f, indent=4
            )

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists)
        """
        if os.path.exists(FileStorage.__file_path) and os.path.getsize(FileStorage.__file_path) > 0:
            with open(FileStorage.__file_path, 'r') as f:
                content = json.load(f)

            for key, value in content.items():
                cls_name = value["__class__"]
                obj = FileStorage.CLASSES[cls_name](**value)
                FileStorage.__objects[key] = obj

