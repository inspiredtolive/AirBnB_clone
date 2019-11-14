#!/usr/bin/python3
"""Test cases for Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """A TestCase for Amenity class."""
    def test_name_exists(self):
        """Tests the default name value."""
        instance = Amenity()
        self.assertEqual(hasattr(instance, "name"), True)
        self.assertIs(type(instance.name), str)
        self.assertEqual(instance.name, "")
