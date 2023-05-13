#!/usr/bin/python3
""" unittest for review module """
import unittest
import datetime
from models.review import Review
from models.user import User
from models.place import Place
from models.base_model import BaseModel
from models import storage


class TestReview(unittest.TestCase):
    """ a test for the Review calss in side review module """
    def test_attributes(self):
        """ tests the attributes of the class """
        u1 = Review()
        dc = {"id": u1.id, "created_at": u1.created_at.isoformat(),
              "updated_at": u1.updated_at.isoformat(), "__class__": "Review"}
        self.assertEqual(u1.to_dict(), dc)

        u2 = Review(**u1.to_dict())
        self.assertEqual(u2.to_dict(), dc)
        self.assertEqual(u2.to_dict(), u1.to_dict())
        self.assertIsNot(u1, u2)

        u3 = Review(**dc)
        self.assertEqual(u3.to_dict(), dc)

        # saving for updating 'updated_at' attribute
        u1.save()
        self.assertNotEqual(dc, u1.to_dict())

        # types of the attributes
        self.assertIsInstance(u1, Review)
        self.assertIsInstance(u1.updated_at, datetime.datetime)
        self.assertIsInstance(u1.created_at, datetime.datetime)
        self.assertIsInstance(u1.id, str)
        self.assertTrue(issubclass(Review, BaseModel))

        # new instance every time
        u1 = Review()
        u2 = Review()
        self.assertNotEqual(u1.id, u2.id)
        self.assertNotEqual(u1.created_at, u2.created_at)
        self.assertNotEqual(u1.updated_at, u2.updated_at)

    def test_str(self):
        """ tests BaseModel string representation """
        b1 = Review()
        self.assertEqual(str(b1), f"[Review] ({b1.id}) {b1.__dict__}")

    def test_to_dict(self):
        """ tests convertion to dict """
        b1 = Review()
        self.assertIsInstance(b1.to_dict(), dict)
        b1.name = "my_name"
        dc = {'id': b1.id, 'created_at': b1.created_at.isoformat(),
              'updated_at': b1.updated_at.isoformat(),
              '__class__': 'Review', "name": "my_name"}
        self.assertEqual(b1.to_dict(), dc)

        b1 = Review()
        b1.name = 'my_name'
        b1.my_number = 89
        dc = {'id': b1.id, 'created_at': b1.created_at.isoformat(),
              'updated_at': b1.updated_at.isoformat(),
              '__class__': 'Review', 'name': 'my_name', 'my_number': 89}
        self.assertEqual(b1.to_dict(), dc)
        a = b1.to_dict()
        self.assertEqual(a['__class__'], "Review")
        self.assertIsInstance(a['created_at'], str)
        self.assertIsInstance(a['updated_at'], str)
        self.assertIsInstance(a['id'], str)

    def test_save(self):
        """ tests the test model """
        b1 = Review()
        b2 = Review()
        a = b1.updated_at
        b1.save()
        c = b1.updated_at
        self.assertNotEqual(a, c)
        b1.save()
        self.assertNotEqual(a, b1.updated_at)

    def test_file_storage_save_and_new(self):
        """ tests FileStorage.new() and FileStorage.save() in vocation
        inside the Review """
        b1 = Review()
        b2 = Review()
        dc = {f"{b1.to_dict()['__class__']}.{b1.id}": b1,
              f"{b2.to_dict()['__class__']}.{b2.id}": b2}
        st_all = storage.all()
        for d in dc:
            self.assertEqual(dc[d].to_dict(), st_all[d].to_dict())
        # for kwarg arguments .new() is not called
        b3 = Review(**b2.to_dict())
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

    def test_review_attributes(self):
        """ tests the uninherited attributes """
        u1 = Review()
        self.assertIsInstance(u1, Review)
        self.assertIsInstance(u1.updated_at, datetime.datetime)
        self.assertIsInstance(u1.created_at, datetime.datetime)
        self.assertIsInstance(u1.id, str)
        self.assertIsInstance(Review.text, str)
        self.assertIsInstance(u1.place_id, str)
        self.assertIsInstance(u1.user_id, str)

        u1.text = "It has a nice landscape"
        dc = {'id': u1.id, 'created_at': u1.created_at.isoformat(),
              'updated_at': u1.updated_at.isoformat(),
              '__class__': 'Review', "text": "It has a nice landscape"}
        self.assertEqual(u1.to_dict(), dc)
        usr1 = User()
        p1 = Place()
        u1.user_id = usr1.id
        u1.place_id = p1.id
        dc = {'id': u1.id, 'created_at': u1.created_at.isoformat(),
              'updated_at': u1.updated_at.isoformat(),
              '__class__': 'Review', "text": "It has a nice landscape",
              'user_id': usr1.id, 'place_id': p1.id}
        self.assertEqual(u1.to_dict(), dc)
