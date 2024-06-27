#!/usr/bin/python3

"""
This script contains tests for the base model of the project.
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suites for the base model of the project.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.my_model = BaseModel()

    def test_init_no_args(self):
        """
        Test that a new instance can be created without any arguments.
        """
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))

    def test_init_with_kwargs(self):
        """
        Test that a new instance can be created with keyword arguments.
        """
        kwargs = {
            "id": "123",
            "name": "ALX",
            "number": 89,
            "created_at": "2021-02-11T09:03:54.052000",
            "updated_at": "2021-02-11T09:03:54.052000",
        }
        mwkwargs = BaseModel(**kwargs)
        self.assertEqual(mwkwargs.id, "123")
        self.assertEqual(mwkwargs.name, "ALX")
        self.assertEqual(mwkwargs.number, 89)
        self.assertIsInstance(mwkwargs.created_at, datetime)
        self.assertIsInstance(mwkwargs.updated_at, datetime)
        self.assertEqual(
            mwkwargs.created_at.isoformat(),
            "2021-02-11T09:03:54.052000"
        )
        self.assertEqual(
            mwkwargs.updated_at.isoformat(),
            "2021-02-11T09:03:54.052000"
        )

    def test_init_with_partial_kwargs(self):
        """
        Test that a new instance can be created with partial keyword arguments.
        """
        kwargs = {"id": "456", "name": "School"}
        model_with_partial_kwargs = BaseModel(**kwargs)
        self.assertEqual(model_with_partial_kwargs.id, "456")
        self.assertEqual(model_with_partial_kwargs.name, "School")
        self.assertFalse(hasattr(model_with_partial_kwargs, "created_at"))
        self.assertFalse(hasattr(model_with_partial_kwargs, "updated_at"))

    def test_init_ignores_class_key_in_kwargs(self):
        """
        Test that __class__ key in kwargs is ignored during initialization.
        """
        kwargs = {"__class__": "ShouldNotBeSet", "id": "789", "name": "Test"}
        mwclass_key = BaseModel(**kwargs)
        self.assertFalse(hasattr(mwclass_key, "__class__ShouldNotBeSet"))
        self.assertEqual(mwclass_key.id, "789")
        self.assertEqual(mwclass_key.name, "Test")
