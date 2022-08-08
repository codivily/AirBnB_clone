#!/usr/bin/env python3
"""Test module for file storage engine"""

import unittest
from models.base_model import BaseModel
from models import storage
import os
import json
import models
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorageEngine(unittest.TestCase):
    """Class for for Unittesting file storage engine"""

    @classmethod
    def setUpClass(cls):
        """Setup the test case"""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    @classmethod
    def tearDownClass(cls):
        """Cleanup after tests done"""
        try:
            os.remove(storage._FileStorage__file_path)
        except Exception:
            pass

    def test_storage_save_objects(self):
        """Test storage.new method"""
        storage.clear()
        storage.reload()
        objects = storage.all()

        self.assertEqual(len(objects), 0)

        obj1 = BaseModel()
        obj2 = BaseModel()

        obj1.save()
        obj2.save()

        self.assertIs(type(storage.all()), dict)
        self.assertEqual(len(storage.all()), 2)

        storage.reload()
        self.assertEqual(len(storage.all()), 2)

class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""
    
    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage.__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage.__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage_methods(unittest.TestCase):
    """Unittests nfor testing methods of the FileStorage class."""

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
        FileStorage.FileStorage__objects = {}

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
         bm = BaseModel()
         us = User()
         st = State()
         pl = Place()
         cy = City()
         am = Amenity()
         rv = Review()
         models.storage.new(bm)
         models.storage.new(us)
         models.storage.new(st)
         models.storage.new(pl)
         models.storage.new(cy)
         models.storage.new(am)
         models.storage.new(rv)
         models.storage.save()
         save_test = ""
         with open("file.json", "r") as f:
             save_text = f.read()
             self.assertIn("BaseModel." + bm.id, save_test)
             self.assertIn("User." + us.id, save_test)
             self.assertIn("State." + st.id, save_test)
             self.assertIn("Place." + pl.id, save_test)
             self.assertIn("City." + cy.id, save_test)
             self.assertIn("Amenity." + am.id, save_test)
             self.assertIn("Review." + rv.id, save_test)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        model.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

if __name__ == "__main__":
    unittest.main()
