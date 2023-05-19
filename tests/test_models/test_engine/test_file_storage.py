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
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_storage(self):
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
        self.assertIsInstance(storage.all(), dict)

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

    def test_reload(self):
        """ it checks the reload method """
        store = FileStorage()
        with open('file.json', 'w') as f:
            f.write('{}')
        store.reload()
        # empty file.json
        remove('file.json')
        store.reload()
        self.assertEqual(store.all(), {})
        # file.json with empty dictionary
        with open('file.json', 'w') as f:
            f.write('{}')
        store.reload()
        self.assertEqual(store.all(), {})
        # file.json with 1 element with out reloading
        b1 = BaseModel()
        st_all = store.all()
        dc = {f"{b1.to_dict()['__class__']}.{b1.id}": b1}
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())
        # reloading with out saving
        store.reload()
        self.assertEqual(store.all(), {})
        # reloading after saving
        b1 = BaseModel()
        st_all = store.all()
        store.save()
        store.reload()
        dc = {f"{b1.to_dict()['__class__']}.{b1.id}": b1}
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())
        # using BaseModel's save
        b2 = BaseModel()
        st_all = store.all()
        b2.save()
        store.reload()
        dc = {f"{b1.to_dict()['__class__']}.{b1.id}": b1,
              f"{b2.to_dict()['__class__']}.{b2.id}": b2}
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())
