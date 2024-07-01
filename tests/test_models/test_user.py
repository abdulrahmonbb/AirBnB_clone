#!/usr/bin/python3

"""
This script contains the unit test for the User class.
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """Create a new User instance before each test."""
        self.user = User()

    def test_initialization(self):
        """Test initialization of User attributes."""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_inheritance(self):
        """Test that User correctly inherits from BaseModel."""
        self.assertIsInstance(self.user, User)

    def test_attribute_types(self):
        """Test the type of User attributes."""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_setting_attributes(self):
        """Test setting User attributes."""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
