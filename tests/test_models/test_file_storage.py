""" this is a test file to test the filestorage class"""


import unittest
from models.base_model import BaseModel
from models import storage
import json


class TestFileStorage(unittest.TestCase):

    def test_file_path(self):
        self.assertIsInstance(storage.file_path, str)
        self.assertEqual(storage.file_path, "file.json")

    def test_objects(self):
        self.assertIsInstance(storage.objects, dict)
        obj = BaseModel()
        storage.new(obj)
        self.assertEqual(storage.objects[f"BaseModel.{obj.id}"], obj)

    def test_all(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(storage.objects[f"BaseModel.{obj1.id}"], obj1)
        self.assertEqual(storage.objects[f"BaseModel.{obj2.id}"], obj2)

    def test_new(self):
        obj = BaseModel()
        storage.new(obj)
        self.assertEqual(storage.objects[f"BaseModel.{obj.id}"], obj)

    def test_save(self):
        o1 = BaseModel()
        o2 = BaseModel()
        storage.new(o1)
        storage.new(o2)
        storage.save()
        storage.reload()
        self.assertIsInstance(storage.objects[f"BaseModel.{o1.id}"], BaseModel)
        self.assertIsInstance(storage.objects[f"BaseModel.{o2.id}"], BaseModel)
