#!/usr/bin/python3

"""
This script contains unittests for the state class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_instance_creation(self):
        """Test the creation of a State instance."""
        my_state = State()
        self.assertIsInstance(my_state, State)

    def test_initial_name_empty(self):
        """Test that the initial name attribute is an empty string."""
        my_state = State()
        self.assertEqual(my_state.name, "")

    def test_name_set(self):
        """Test setting the name attribute."""
        my_state = State()
        my_state.name = "California"
        self.assertEqual(my_state.name, "California")

    def test_inheritance_from_BaseModel(self):
        """Test if State instances inherit from BaseModel."""
        my_state = State()
        self.assertTrue(hasattr(my_state, "id"))
        self.assertTrue(hasattr(my_state, "created_at"))
        self.assertTrue(hasattr(my_state, "updated_at"))


if __name__ == "__main__":
    unittest.main()
