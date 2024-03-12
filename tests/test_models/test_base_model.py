""" this is a test file to test the BaseModel class"""


import unittest
from models.base_model import BaseModel
from io import StringIO
import datetime
import sys


class TestBaseModel(unittest.TestCase):
    """ test base model"""

    def test_init(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)

    def test_str(self):
        my_model = BaseModel()
        ex = f"[{type(my_model).__name__}] ({my_model.id} {my_model.__dict__}"
        self.assertEqual(str(my_model), ex)

    def test_save(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertGreater(my_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertEqual(my_dict["__class__"], type(my_model).__name__)
        self.assertIsInstance(my_dict["created_at"], str)
        self.assertIsInstance(my_dict["updated_at"], str)
