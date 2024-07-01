#!/usr/bin/python3

"""
This script contains the review class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review.

    Attributes:
        place_id (str): The review's place ID.
        user_id (str): The review's user ID.
        text (str): The review's text.
    """

    place_id = ""
    user_id = ""
    text = ""
