#!/usr/bin/python3
""" unittest for city module """
import unittest
import datetime
from models.city import City
from models.state import State
from models.base_model import BaseModel
from models import storage


class TestCity(unittest.TestCase):
    """ a test for the City calss in side city module """
    def test_attributes(self):
        """ tests the attributes of the class """
        u1 = City()
        dc = {"id": u1.id, "created_at": u1.created_at.isoformat(),
              "updated_at": u1.updated_at.isoformat(), "__class__": "City"}
        self.assertEqual(u1.to_dict(), dc)

        u2 = City(**u1.to_dict())
        self.assertEqual(u2.to_dict(), dc)
        self.assertEqual(u2.to_dict(), u1.to_dict())
        self.assertIsNot(u1, u2)

        u3 = City(**dc)
        self.assertEqual(u3.to_dict(), dc)

        # saving for updating 'updated_at' attribute
        u1.save()
        self.assertNotEqual(dc, u1.to_dict())

        # types of the attributes
        self.assertIsInstance(u1, City)
        self.assertIsInstance(u1.updated_at, datetime.datetime)
        self.assertIsInstance(u1.created_at, datetime.datetime)
        self.assertIsInstance(u1.id, str)
        self.assertTrue(issubclass(City, BaseModel))

        # new instance every time
        u1 = City()
        u2 = City()
        self.assertNotEqual(u1.id, u2.id)
        self.assertNotEqual(u1.created_at, u2.created_at)
        self.assertNotEqual(u1.updated_at, u2.updated_at)

    def test_str(self):
        """ tests BaseModel string representation """
        b1 = City()
        self.assertEqual(str(b1), f"[City] ({b1.id}) {b1.__dict__}")

    def test_to_dict(self):
        """ tests convertion to dict """
        b1 = City()
        self.assertIsInstance(b1.to_dict(), dict)
        b1.name = "my_name"
        dc = {'id': b1.id, 'created_at': b1.created_at.isoformat(),
              'updated_at': b1.updated_at.isoformat(),
              '__class__': 'City', "name": "my_name"}
        self.assertEqual(b1.to_dict(), dc)

        b1 = City()
        b1.name = 'my_name'
        b1.my_number = 89
        dc = {'id': b1.id, 'created_at': b1.created_at.isoformat(),
              'updated_at': b1.updated_at.isoformat(),
              '__class__': 'City', 'name': 'my_name', 'my_number': 89}
        self.assertEqual(b1.to_dict(), dc)
        a = b1.to_dict()
        self.assertEqual(a['__class__'], "City")
        self.assertIsInstance(a['created_at'], str)
        self.assertIsInstance(a['updated_at'], str)
        self.assertIsInstance(a['id'], str)

    def test_save(self):
        """ tests the test model """
        b1 = City()
        b2 = City()
        a = b1.updated_at
        b1.save()
        c = b1.updated_at
        self.assertNotEqual(a, c)
        b1.save()
        self.assertNotEqual(a, b1.updated_at)

    def test_file_storage_save_and_new(self):
        """ tests FileStorage.new() and FileStorage.save() in vocation
        inside the City """
        b1 = City()
        b2 = City()
        dc = {f"{b1.to_dict()['__class__']}.{b1.id}": b1,
              f"{b2.to_dict()['__class__']}.{b2.id}": b2}
        st_all = storage.all()
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())
        # for kwarg arguments .new() is not called
        b3 = City(**b2.to_dict())
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

    def test_city_attributes(self):
        """ tests the uninherited attributes """
        u1 = City()
        self.assertIsInstance(u1, City)
        self.assertIsInstance(u1.updated_at, datetime.datetime)
        self.assertIsInstance(u1.created_at, datetime.datetime)
        self.assertIsInstance(u1.id, str)
        self.assertIsInstance(u1.state_id, str)
        self.assertIsInstance(u1.name, str)

        u1.name = "diredawa"
        dc = {'id': u1.id, 'created_at': u1.created_at.isoformat(),
              'updated_at': u1.updated_at.isoformat(),
              '__class__': 'City', "name": "diredawa"}
        self.assertEqual(u1.to_dict(), dc)
        st1 = State()
        u1.state_id = st1.id
        dc = {'id': u1.id, 'created_at': u1.created_at.isoformat(),
              'updated_at': u1.updated_at.isoformat(),
              '__class__': 'City', "name": "diredawa",
              "state_id": st1.id}
        self.assertEqual(u1.to_dict(), dc)
