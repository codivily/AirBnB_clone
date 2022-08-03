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

    def test_no_arg(self):
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)

    def test_two_basemodels(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

if __name__ == "__main__":
    unittest.main()
