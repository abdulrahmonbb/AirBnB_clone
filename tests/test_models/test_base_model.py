#!/usr/bin/python3

"""
This script contains tests for the base model.
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suites for the base model.
    """

    def setUp(self):
        """
        Classes needed for testing
        """
        self.my_model = BaseModel()

    def test_basic(self):
        """
        Tests basic inputs for the base model class
        """
        self.my_model = my_model
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number], ["ALX", 89])
        self.assertIsInstance(my_model.id, str)

    def test_datetime(self):
        """
        Tests for correct datetime format.
        """
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_to_dict(self):
        """
        Tests for the correct return type of the to_dict method.
        """
        model_dict = self.my_model.to_dict()
        self.assertIsInstance(model_dict, dict)


if __name__ == '__main__':
    unittest.main()
