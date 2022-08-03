#!/usr/bin/python3
# test_base_model.py
"""Defines unittests for base_model.py.

Unittest classes:
    TestBaseModel_Instantiation - line 15
    TestBase_Instance_Print - line 51
    TestBase_Save_Method - line 59
    TestBase_from_json_string - line 234
"""
from datetime import datetime
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

class TestBaseModel_Instance_Print(unittest.TestCase):
    """Unittest for testing the return value of __str__ method."""

    def test_str_return(self):
        b1 = BaseModel()
        ret = "[{}] ({}) {}".format("BaseModel", b1.id, str(b1.__dict__))
        self.assertEqual(print(b1), print(ret))

class TestBaseModel_Save_Method(unittest.TestCase):
    """Unittest for testing the save method."""

    def test_validates_save(self):
        b1 = BaseModel()
        updated_at_1 = b1.updated_at
        b1.save()
        updated_at_2 = b1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

class TestBaseModel_to_Dict_Method(unittest.TestCase):
    """Unittest for testing the to_dict method."""

    def test_validates_to_dict(self):
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertEqual(dic, b1.__dict__)

    def test_className_present(self):
        b1 = BaseModel()
        dic = b1.to_dict()
        className = {"__class__": "BaseModel"}
        assertEqual(dic, dic | className)

if __name__ == "__main__":
    unittest.main()
