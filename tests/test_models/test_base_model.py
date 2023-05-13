#!/usr/bin/python3
""" unittest for the module base_model.py """
import unittest
from models.base_model import BaseModel
from models import storage
import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """ a TestCase for BaseModel """
    def test_attributes(self):
        """ test the attributes assignment and type """
        for i in range(20):
            b1 = BaseModel()
            b2 = BaseModel()
            self.assertNotEqual(b1.id, b2.id)

        # new attribute
        b1.name = 'my_name'
        self.assertIsNotNone(b1.name)

        # types of the attributes
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b1.updated_at, datetime.datetime)
        self.assertIsInstance(b1.created_at, datetime.datetime)
        self.assertIsInstance(b1.id, str)

    def test_save(self):
        """ tests the test model """
        b1 = BaseModel()
        b2 = BaseModel()
        a = b1.updated_at
        b1.save()
        c = b1.updated_at
        self.assertNotEqual(a, c)
        b1.save()
        self.assertNotEqual(a, b1.updated_at)

    def test_file_storage_save_and_new(self):
        """ tests FileStorage.new() and FileStorage.save() in vocation
        inside the BaseModel """
        b1 = BaseModel()
        b2 = BaseModel()
        dc = {f"{b1.to_dict()['__class__']}.{b1.id}": b1,
              f"{b2.to_dict()['__class__']}.{b2.id}": b2}
        st_all = storage.all()
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())
        # for kwarg arguments .new() is not called
        b3 = BaseModel(**b2.to_dict())
        st_all = storage.all()
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())
        # saving to a file using BaseModel.save()
        with open('file.json', 'w') as f:
            f.write('{}')
        b1.save()
        b2.save()
        storage.reload()
        st_all = storage.all()
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())

    def test_str(self):
        """ tests BaseModel string representation """
        b1 = BaseModel()
        self.assertEqual(str(b1), f"[BaseModel] ({b1.id}) {b1.__dict__}")

    def test_to_dict(self):
        """ tests convertion to dict """
        b1 = BaseModel()
        self.assertIsInstance(b1.to_dict(), dict)
        dc = {'id': b1.id, 'created_at': b1.created_at.isoformat(),
              'updated_at': b1.updated_at.isoformat(),
              '__class__': 'BaseModel'}
        self.assertEqual(b1.to_dict(), dc)

        b1 = BaseModel()
        self.assertIsInstance(b1.to_dict(), dict)
        b1.name = 'my_name'
        b1.my_number = 89
        dc = {'id': b1.id, 'created_at': b1.created_at.isoformat(),
              'updated_at': b1.updated_at.isoformat(),
              '__class__': 'BaseModel', 'name': 'my_name', 'my_number': 89}
        self.assertEqual(b1.to_dict(), dc)
        a = b1.to_dict()
        self.assertIn('__class__', a)
        self.assertIsInstance(a['created_at'], str)
        self.assertIsInstance(a['updated_at'], str)
        self.assertIsInstance(a['id'], str)

    def test_basemodels_with_arguments(self):
        """ tests BaseModel with kwargs as parameter """
        b1 = BaseModel()
        b2 = BaseModel(**b1.to_dict())
        self.assertIsNot(b1, b2)
        self.assertEqual(b1.to_dict(), b2.to_dict())

        b1.name = "my_name"
        b2 = BaseModel(**b1.to_dict())
        self.assertEqual(b1.to_dict(), b2.to_dict())

        b1.save()
        self.assertNotEqual(b1.to_dict(), b2.to_dict())

        b2 = BaseModel(**b1.to_dict())
        self.assertEqual(b1.to_dict(), b2.to_dict())
        self.assertIsInstance(b2.updated_at, datetime.datetime)
        self.assertIsInstance(b2.created_at, datetime.datetime)
        self.assertIsInstance(b2.id, str)
