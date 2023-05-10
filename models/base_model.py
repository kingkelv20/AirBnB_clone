#!/usr/bin/python3
"""
    a base model that defines all common attributes for other classes
"""
import datetime
import uuid
import models


class BaseModel:
    """ a BaseModel class that defines all common attributes and methods
        for other classes
    """
    def __init__(self, *args, **kwargs):
        """ initializes the values """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            if '__class__' in kwargs:
                kwargs.pop('__class__')
            self.__dict__ = kwargs
            self.created_at = datetime.datetime.strptime(
                              kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.datetime.strptime(
                              kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """ string representation of the class used """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the updated_at attribute """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary representation of the given class """
        temp = self.__dict__.copy()
        temp['__class__'] = type(self).__name__
        temp['updated_at'] = self.updated_at.isoformat()
        temp['created_at'] = self.created_at.isoformat()
        return temp
