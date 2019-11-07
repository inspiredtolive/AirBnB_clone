#!/usr/bin/python3
"""Defines all attributes and methods for BaseModel"""
import uuid
import datetime

class BaseModel:
    """BaseModel class"""

    def __init__(self):
        """Initialize"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return string format of instance"""
        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id,\
                                       self.__dict__)

    def save(self):
        """Update updated_at attribute with current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return dictionary containing all key/value of __dict__ of instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
