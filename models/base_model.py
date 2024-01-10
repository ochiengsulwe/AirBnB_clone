#!/usr/bin/python3
"""Defines a class Basemodel that all my objects will inherit from"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Class that defines universal properties of my instances """

    def __init__(self, *args, **kwargs):
        """ Creates new instances of Base.

        Args:
            *args (list): a list of variable number of arguments.
                All attributes are automatically assigned upon instantiation.
            **kwargs (dict): a dictionary of instance attributes.
                This is invoked during the instance update.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()
        else:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for (key, value) in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns a string represation of class details.

        Returns:
            str: class details
        """
        return f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """Update public instance attribute updated_at with current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance.

        Returns:
            dict: key/value pairs.
        """
        dict_ = self.__dict__.copy()
        dict_['__class__'] = self.__class__.__name__
        dict_['created_at'] = self.created_at.isoformat()
        dict_['updated_at'] = self.updated_at.isoformat()
        return dict_
