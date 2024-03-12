"""this file tests the state class """

import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_init_no_attr(self):
        s = State()
        self.assertEqual(len(s.name), 0)

    def test_init_with_attr(self):
        s2 = State("name")
        self.assertEqual(s2.name, "name")
