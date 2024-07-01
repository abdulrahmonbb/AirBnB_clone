#!/usr/bin/python3

"""
This script contains the amenity class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity.

    Attributes:
        name (str): The amenity's name.
    """

    name = ""
    