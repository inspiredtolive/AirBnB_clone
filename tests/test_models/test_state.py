#!/usr/bin/python3
"""Test cases for State class."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """A TestCase for State class."""
    def test_inherits_BaseModel(self):
        """Tests if State inherits from BaseModel."""
        instance = State()
        self.assertIsInstance(instance, BaseModel)

    def test_name_exists(self):
        """Tests the default name value."""
        self.assertEqual(hasattr(State, "name"), True)
        self.assertIs(type(State.name), str)
        self.assertEqual(State.name, "")
