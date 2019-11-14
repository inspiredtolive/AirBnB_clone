#!/usr/bin/python3
"""Defines a TestCase for BaseModel."""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Defines individual tests for FileStorage."""
    def setUp(self):
        """Creates FileStorage instance and sets file_path to test.json."""
        self.storage = FileStorage()
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}
        self.storage.reload()

    def tearDown(self):
        """Deletes the test json file."""
        if os.path.exists("test.json"):
            os.remove("test.json")

    def test_file_path_exists(self):
        """Tests for __file_path value."""
        self.assertEqual(hasattr(FileStorage, "_FileStorage__file_path"), True)
        self.assertIs(type(FileStorage._FileStorage__file_path), str)

    def test_objects_exists(self):
        """Tests for __objects value."""
        self.assertEqual(hasattr(FileStorage, "_FileStorage__objects"), True)
        self.assertIs(type(FileStorage._FileStorage__objects), dict)
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_all_default(self):
        """Tests all with default __objects."""
        self.assertIs(type(self.storage.all()), dict)
        self.assertEqual(self.storage.all(), {})

    def test_all_BaseModel_instance(self):
        """Tests all with one BaseModel instance."""
        instance = BaseModel()
        self.assertIs(type(self.storage.all()), dict)
        self.assertEqual(self.storage.all(), {
            "BaseModel." + instance.id: instance
        })

    def test_new(self):
        """Test new with a BaseModel instance."""
        my_dict = {
            "__class__": "BaseModel",
            "id": "5e2d1d8d-92e5-4bc5-ad9a-991ef2268eb8",
            "updated_at": "2019-11-08T23:23:15.141214",
            "created_at": "2019-11-08T23:23:15.141191"
        }
        key = "BaseModel.5e2d1d8d-92e5-4bc5-ad9a-991ef2268eb8"
        instance = BaseModel(**my_dict)
        self.storage.new(instance)
        self.assertIn(key, self.storage.all())
        self.assertIs(self.storage.all()[key], instance)

    def test_save(self):
        """Test save with a BaseModel instance."""
        my_dict = {
            "__class__": "BaseModel",
            "id": "5e2d1d8d-92e5-4bc5-ad9a-991ef2268eb8",
            "updated_at": "2019-11-08T23:23:15.141214",
            "created_at": "2019-11-08T23:23:15.141191"
        }
        key = "BaseModel.5e2d1d8d-92e5-4bc5-ad9a-991ef2268eb8"
        expected = {key: my_dict}
        instance = BaseModel(**my_dict)
        self.storage.new(instance)
        self.storage.save()
        with open("test.json", "r") as f:
            json_dict = json.load(f)
            self.assertEqual(json_dict, expected)

    def test_reload(self):
        """Test save with a BaseModel instance."""
        my_dict = {
            "__class__": "BaseModel",
            "id": "5e2d1d8d-92e5-4bc5-ad9a-991ef2268eb8",
            "updated_at": "2019-11-08T23:23:15.141214",
            "created_at": "2019-11-08T23:23:15.141191"
        }
        key = "BaseModel.5e2d1d8d-92e5-4bc5-ad9a-991ef2268eb8"
        instance = BaseModel(**my_dict)
        self.storage.new(instance)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all().keys()), 1)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].to_dict(), my_dict)


if __name__ == '__main__':
    unittest.main()
