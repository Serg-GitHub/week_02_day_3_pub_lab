import unittest
from src.drinks import *
from src.pub import *
from src.customer import *

class TestDrinks(unittest.TestCase):

    def setUp(self):
        self.drink = Drinks("Beer", 5)
        

    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink.name) 
      