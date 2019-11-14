#!/usr/bin/python3
"""Test cases for City class."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """A TestCase for City class."""
    def test_state_id_exists(self):
        """Tests the default state_id value."""
        instance = City()
        self.assertEqual(hasattr(instance, "state_id"), True)
        self.assertIs(type(instance.state_id), str)
        self.assertEqual(instance.state_id, "")

    def test_name_exists(self):
        """Tests the default name value."""
        instance = City()
        self.assertEqual(hasattr(instance, "name"), True)
        self.assertIs(type(instance.name), str)
        self.assertEqual(instance.name, "")

    def test_inherits_BaseModel(self):
        """Tests if City inherits from BaseModel."""
        instance = City()
        self.assertIsInstance(instance, BaseModel)
