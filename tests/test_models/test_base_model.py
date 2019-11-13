#!/usr/bin/python3
"""Defines a TestCase for BaseModel."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Defines individual tests for BaseModel."""
    def setUp(self):
        """Creates FileStorage instance and sets file_path to test.json."""
        self.storage = FileStorage()
        FileStorage._FileStorage__file_path = "test.json"
        self.storage.reload()

    def test_id_string_type(self):
        """Tests if the ID is a string."""
        self.assertEqual(type(BaseModel().id), str)

    def test_id_unique(self):
        """Tests if the IDs are unique."""
        unique_ids = set()
        for i in range(1000):
            instance = BaseModel()
            self.assertEqual(instance.id in unique_ids, False)
            unique_ids.add(instance.id)

if __name__ == '__main__':
    unittest.main()
