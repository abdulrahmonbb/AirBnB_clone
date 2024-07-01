#!/usr/bin/python3

"""
This script contains the state class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state.

    Attributes:
        name (str): The state's name.
    """

    name = ""
