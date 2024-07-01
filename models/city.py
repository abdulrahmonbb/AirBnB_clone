#!/usr/bin/python3

"""
This script contains the city class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city.

    Attributes:
        state_id (str): The city's state ID.
        name (str): The city's name.
    """

    state_id = ""
    name = ""
