#!/usr/bin/python3
""" a unittest for the module models/engine/file_storage.py """
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import json
from os import remove
from os.path import exists


class TestFileStorage(unittest.TestCase):
    """ tests the file storage """
    def test_reload(self):
        """ tests the reload, save, new and all methods"""
        # starting with empty dictionary json file
        with open('file.json', 'w') as f:
            f.write('{}')
        storage.reload()
        self.assertEqual(storage.all(), {})

        # new one element
        b1 = BaseModel()
        storage.new(b1)
        dc = {f"{b1.to_dict()['__class__']}.{b1.id}": b1}
        self.assertEqual(storage.all(), dc)

        # if file doesn't exist do nothing
        remove('file.json')
        storage.reload()
        self.assertEqual(storage.all(), dc)

        # adding a second new element
        b2 = BaseModel(**b1.to_dict())
        storage.new(b2)
        dc = {f"{b1.to_dict()['__class__']}.{b1.id}": b1,
              f"{b2.to_dict()['__class__']}.{b2.id}": b2}
        self.assertEqual(dc, storage.all())

        # saving and reloading
        storage.save()
        storage.reload()
        st_all = storage.all()
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())

        # removing and resaving the objects to a file
        remove('file.json')
        storage.save()
        storage.reload()
        st_all = storage.all()
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())

        # creating a new FileStorage instance testing for Class attributes
        new_store = FileStorage()
        new_store.reload()
        st_all = storage.all()
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())
