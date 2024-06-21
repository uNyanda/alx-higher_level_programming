#!/usr/bin/python3
"""
This module contains unittests for the 'Base' class.
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """
    Defines a class to test the 'Base' class.
    """

    def setUp(self):
        """
        Resets the 'Base' class's '__nb_objects' counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """
        Tests the id assignment in the 'Base' class.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(100)
        self.assertEqual(b3.id, 100)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_multiple_instances(self):
        """
        Tests the id increment for multiple instances of the 'Base' class.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_none_and_nb_objects_increment(self):
        """
        Tests if id is None, __nb_objects increments, and id equals __nb_objects.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.id, Base._Base__nb_objects)

        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.id, Base._Base__nb_objects)


if __name__ == "__main__":
    unittest.main()
