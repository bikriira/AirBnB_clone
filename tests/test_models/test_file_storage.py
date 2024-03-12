""" this is a test file to test the filestorage class"""


import unittest
from models.base_model import BaseModel
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):

    def test_file_path(self):
        self.assertIsInstance(storage.file_path, str)

    def test_objects(self):
        self.assertIsInstance(storage.objects, dict)

    def test_all(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        Storage.new(obj1)
        storage.new(obj2)
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), len(storage.objects))

    def test_new(self):
        obj = BaseModel()
        storage.new(obj)
        self.assertIsInstance(storage.objects[f"{obj.__class__.__name__}.{obj.id}"], BaseModel)

    def test_save(self):
        o1 = BaseModel()
        o2 = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists(storage.file_path))
        with open(storage.file_path, "w", encoding="utf-8") as f:
            loaded_data = json.load(f)
        self.assertEqual(loaded_data[f"BaseModel.{o1.id}"], o1.to_dict())

    def test_reload(self):

