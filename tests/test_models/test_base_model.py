#!/usr/bin/python3
# test_base_model.py
"""Defines unittests for base_model.py.

Unittest classes:
    TestBaseModel_instantiation - line 16
    TestBase_to_json_string - line 98
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel_Instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_IsInstanceOf(self):
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_ContainsId(self):
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "id"))

    def test_IdType(self):
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)

    def test_CompareTwoInstancesId(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_ContainsCreated_at(self):
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "created_at"))

    def test_Created_atInstance(self):
        b1 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)

    def test_ContainsUpdated_at(self):
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "updated_at"))

    def test_Created_atInstance(self):
        b1 = BaseModel()
        self.assertIsInstance(b1.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
