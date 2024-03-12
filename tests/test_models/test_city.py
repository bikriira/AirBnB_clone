""" this file is to test the City class"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_init_city_noattr(self):
        c1 = City()
        self.assertEqual(len(c1.state_id), 0)
        self.assertEqual(len(c1.name), 0)

    def test_init_city_attr(self):
        c2 = City("24", "guelma")
