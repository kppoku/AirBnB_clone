#!/usr/bin/python3
"""This module defines a base class
for all models in our hbnb clone
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class
    for all hbnb models
    """

    def __init__(self, *args, **kwargs):
        """checks if their is
        keyword argument or otherwise
        """

        if kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            return

        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                self.__dict__[key] = datetime.fromisoformat(value)
            elif key != '__class__':
                self.__dict__[key] = value

    def __str__(self):
        """it return a string
        representation of an instance
        """

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with
        current time when instance is changed
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert instance
        into dict format
        """

        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
