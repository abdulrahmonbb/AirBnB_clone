#!/usr/bin/python3

"""
This script contains the place class that inherits from BaseModel.
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place.

    Attributes:
        city_id (str): The place's city ID.
        user_id (str): The place's user ID.
        name (str): The place's name.
        description (str): The place's description.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests in the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The place's latitude.
        longitude (float): The place's longitude.
        amenity_ids (list): A list of amenity IDs.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
