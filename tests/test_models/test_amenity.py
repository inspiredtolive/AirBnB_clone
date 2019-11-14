#!/usr/bin/python3
"""Test cases for Amenity class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """A TestCase for Amenity class."""
    def test_inherits_BaseModel(self):
        """Tests if Amenity inherits from BaseModel."""
        instance = Amenity()
        self.assertIsInstance(instance, BaseModel)

    def test_name_exists(self):
        """Tests the default name value."""
        self.assertEqual(hasattr(Amenity, "name"), True)
        self.assertIs(type(Amenity.name), str)
        self.assertEqual(Amenity.name, "")
