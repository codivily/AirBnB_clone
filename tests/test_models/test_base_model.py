#!/usr/bin/python3
# test_base_model.py
"""Defines unittests for base_model.py.

Unittest classes:
    TestBaseModel_Instantiation - line 15
    TestBase_Instance_Print - line 51
    TestBase_Save_Method - line 59
    TestBase_from_json_string - line 234
"""
from datetime import datetime, timezone
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
        self.assertEqual(str(b1), ret)


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

    def test_className_present(self):
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertNotEqual(dic, b1.__dict__)

    def test_attribute_ISO_format(self):
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)


class TestBaseModel_Kwargs(unittest.TestCase):
    """Unittest for instantiating BaseModel from kwargs"""

    def test_recreate(self):
        """Test BaseModel instantiation from kwargs"""
        b1 = BaseModel()
        b1.my_number = 89

        b2 = BaseModel(**b1.to_dict())
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.my_number, b2.my_number)
        self.assertEqual(b2.created_at.isoformat(), b2.created_at.isoformat())
        self.assertEqual(b1.updated_at.isoformat(), b2.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
