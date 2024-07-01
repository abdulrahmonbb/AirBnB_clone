#!/usr/bin/python3

"""
This script contains unittests for the review class.
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """Create an instance of Review before each test."""
        self.review = Review()

    def test_instance_creation(self):
        """Test if the instance is correctly created and inherits from
        BaseModel."""
        self.assertIsInstance(self.review, Review)

    def test_initial_attributes(self):
        """Test if attributes are initialized correctly."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attribute_assignment(self):
        """Test assigning values to attributes."""
        self.review.place_id = "some_place_id"
        self.review.user_id = "some_user_id"
        self.review.text = "some_text"
        self.assertEqual(self.review.place_id, "some_place_id")
        self.assertEqual(self.review.user_id, "some_user_id")
        self.assertEqual(self.review.text, "some_text")


if __name__ == "__main__":
    unittest.main()
