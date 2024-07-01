#!/usr/bin/python3

"""
This module contains the test suite for the City class.
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        """Create a new City instance before each test."""
        self.city = City()

    def test_initialization(self):
        """Test initialization of City attributes."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_inheritance(self):
        """Test that City correctly inherits from BaseModel."""
        self.assertIsInstance(self.city, City)

    def test_attribute_types(self):
        """Test the type of City attributes."""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_setting_attributes(self):
        """Test setting City attributes."""
        self.city.state_id = "state123"
        self.city.name = "Springfield"
        self.assertEqual(self.city.state_id, "state123")
        self.assertEqual(self.city.name, "Springfield")


if __name__ == "__main__":
    unittest.main()
