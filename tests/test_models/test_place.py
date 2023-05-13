#!/usr/bin/python3
""" unittest for place module """
import unittest
import datetime
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage


class TestPlace(unittest.TestCase):
    """ a test for the Place calss in side place module """
    def test_attributes(self):
        """ tests the attributes of the class """
        u1 = Place()
        dc = {"id": u1.id, "created_at": u1.created_at.isoformat(),
              "updated_at": u1.updated_at.isoformat(), "__class__": "Place"}
        self.assertEqual(u1.to_dict(), dc)

        u2 = Place(**u1.to_dict())
        self.assertEqual(u2.to_dict(), dc)
        self.assertEqual(u2.to_dict(), u1.to_dict())
        self.assertIsNot(u1, u2)

        u3 = Place(**dc)
        self.assertEqual(u3.to_dict(), dc)

        # saving for updating 'updated_at' attribute
        u1.save()
        self.assertNotEqual(dc, u1.to_dict())

        # types of the attributes
        self.assertIsInstance(u1, Place)
        self.assertIsInstance(u1.updated_at, datetime.datetime)
        self.assertIsInstance(u1.created_at, datetime.datetime)
        self.assertIsInstance(u1.id, str)
        self.assertTrue(issubclass(Place, BaseModel))

        # new instance every time
        u1 = Place()
        u2 = Place()
        self.assertNotEqual(u1.id, u2.id)
        self.assertNotEqual(u1.created_at, u2.created_at)
        self.assertNotEqual(u1.updated_at, u2.updated_at)

    def test_str(self):
        """ tests BaseModel string representation """
        b1 = Place()
        self.assertEqual(str(b1), f"[Place] ({b1.id}) {b1.__dict__}")

    def test_to_dict(self):
        """ tests convertion to dict """
        b1 = Place()
        self.assertIsInstance(b1.to_dict(), dict)
        b1.name = "my_name"
        dc = {'id': b1.id, 'created_at': b1.created_at.isoformat(),
              'updated_at': b1.updated_at.isoformat(),
              '__class__': 'Place', "name": "my_name"}
        self.assertEqual(b1.to_dict(), dc)

        b1 = Place()
        b1.name = 'my_name'
        b1.my_number = 89
        dc = {'id': b1.id, 'created_at': b1.created_at.isoformat(),
              'updated_at': b1.updated_at.isoformat(),
              '__class__': 'Place', 'name': 'my_name', 'my_number': 89}
        self.assertEqual(b1.to_dict(), dc)
        a = b1.to_dict()
        self.assertEqual(a['__class__'], "Place")
        self.assertIsInstance(a['created_at'], str)
        self.assertIsInstance(a['updated_at'], str)
        self.assertIsInstance(a['id'], str)

    def test_save(self):
        """ tests the test model """
        b1 = Place()
        b2 = Place()
        a = b1.updated_at
        b1.save()
        c = b1.updated_at
        self.assertNotEqual(a, c)
        b1.save()
        self.assertNotEqual(a, b1.updated_at)

    def test_file_storage_save_and_new(self):
        """ tests FileStorage.new() and FileStorage.save() in vocation
        inside the Place """
        b1 = Place()
        b2 = Place()
        dc = {f"{b1.to_dict()['__class__']}.{b1.id}": b1,
              f"{b2.to_dict()['__class__']}.{b2.id}": b2}
        st_all = storage.all()
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())
        # for kwarg arguments .new() is not called
        b3 = Place(**b2.to_dict())
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

    def test_place_attributes(self):
        """ tests the uninherited attributes """
        self.maxDiff = None
        u1 = Place()
        self.assertIsInstance(u1, Place)
        self.assertIsInstance(u1.updated_at, datetime.datetime)
        self.assertIsInstance(u1.created_at, datetime.datetime)
        self.assertIsInstance(u1.id, str)
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(u1.user_id, str)
        self.assertIsInstance(u1.name, str)
        self.assertIsInstance(u1.description, str)
        self.assertIsInstance(u1.number_rooms, int)
        self.assertIsInstance(u1.number_bathrooms, int)
        self.assertIsInstance(u1.max_guest, int)
        self.assertIsInstance(u1.price_by_night, int)
        self.assertIsInstance(u1.latitude, float)
        self.assertIsInstance(u1.longitude, float)
        self.assertIsInstance(u1.amenity_ids, list)

        u1.name = "Lee"
        dc = {'id': u1.id, 'created_at': u1.created_at.isoformat(),
              'updated_at': u1.updated_at.isoformat(),
              '__class__': 'Place', "name": "Lee"}
        self.assertEqual(u1.to_dict(), dc)
        c1 = City()
        usr1 = User()
        a1 = Amenity()
        a2 = Amenity()
        u1.city_id = c1.id
        u1.user_id = usr1.id
        u1.description = "this is a description of a place"
        u1.number_rooms = 3
        u1.number_bathrooms = 1
        u1.max_guest = 4
        u1.price_by_night = 400
        u1.latitude = 567.57
        u1.longitude = 431.77
        u1.amenity_ids = [a1.id, a2.id]
        dc = {'id': u1.id, 'created_at': u1.created_at.isoformat(),
              'updated_at': u1.updated_at.isoformat(),
              '__class__': 'Place', "name": "Lee", "city_id": c1.id,
              'user_id': usr1.id, "number_rooms": 3, "latitude": 567.57,
              "number_bathrooms": 1, "max_guest": 4, "longitude": 431.77,
              'description': "this is a description of a place",
              'amenity_ids': [a1.id, a2.id], 'price_by_night': 400}
        self.assertEqual(u1.to_dict(), dc)
