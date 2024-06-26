#!/usr/bin/python3

"""
This script contains the base model for the whole project.
"""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """
    Represents the base model from which other models in
    the project inherit from.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of the instances of this object.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the attributes
        of the instance as key/value pairs.
        """
        to_json = self.__dict__.copy()
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] = self.created_at.isoformat()
        to_json['updated_at'] = self.updated_at.isoformat()
        return to_json

    def __str__(self):
        """
        Prints a string representation of the instance so it is human readable.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
