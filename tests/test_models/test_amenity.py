#!/usr/bin/python3

"""
This script contains unittests for the amenity class.
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_instance_creation(self):
        """Test the creation of an Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_initial_name(self):
        """Test if the initial name is an empty string."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name_set(self):
        """Test setting the name attribute."""
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

    def test_inheritance_from_BaseModel(self):
        """Test if Amenity correctly inherits from BaseModel."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))


if __name__ == "__main__":
    unittest.main()
