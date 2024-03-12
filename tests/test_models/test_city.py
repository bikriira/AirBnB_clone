""" this file is to test the City class"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_init_city_noattr(self):
        c1 = City()
        self.assertEqual(c1.state_id, "State.id")
        self.assertEqual(c1.name, "")

    def test_init_city_attr(self):
        c2 = City("24", "guelma")
        self.assertEqual(c2.state_id, "24")
        self.assertEqual(c2.name, "guelma")
