#!/usr/bin/python3

"""
This script contains the file storage which serializes instances to a JSON file
and deserializes JSON file to instances.
"""

import os
import json


class FileStorage:
    """
    Represents the file storage for the project.
    """

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """
        Returns a dictionary of classes.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        ser_obj = {}
        for key, value in self.__objects.items():
            ser_obj[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(ser_obj, f, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists)
        """
        if os.path.exists(self.__file_path) and \
                os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, "r") as f:
                content = json.load(f)

            for key, value in content.items():
                cls_name = value["__class__"]
                obj = self.classes()[cls_name](**value)
                self.__objects[key] = obj
