#!/usr/bin/env python3
"""Test module for file storage engine"""

import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os

class TestFileStorageEngine(unittest.TestCase):
    """Class for for Unittesting file storage engine"""

    @classmethod
    def setUpClass(cls):
        """Setup the test case"""
        FileStorage.__file_path = "data.json"

    @classmethod
    def tearDownClass(cls):
        """Cleanup after tests done"""
        os.remove(FileStorage.__file_path)

    def test_storage_save_objects(self):
        """Test storage.new method"""
        obj1 = BaseModel()
        obj2 = BaseModel()

        obj1.save()
        obj2.save()

        objects = storage.all()

        self.assertIs(objects, dict)
        self.assertEqual(len(objects), 2)

        self.assertEqual(obj1.id in objects, True)
        self.assertEqual(obj2.id in objects, True)

        self.assertEqual(objects.get(obj1.id) is obj1, True)
        self.assertEqual(objects.get(obj2.id) is obj2, True)


        storage.reload()
        objects2 = storage.all()
        self.assertEqual(objects is objects2, False)
