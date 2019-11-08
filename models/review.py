#!/usr/bin/python3
"""Define all attributes and methods for Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""
