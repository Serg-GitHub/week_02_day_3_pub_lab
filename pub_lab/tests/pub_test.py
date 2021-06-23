import unittest
from src.pub import *
from src.customer import *
from src.drinks import *

class TestPub(unittest.TestCase):
    

   def setUp(self):
       self.pub = Pub("The Prancing Pony", 100, [])
       self.drink = Drinks("Beer", 5)
       self.customer = Customer("Craig Smith")
    

   def test_pub_has_name(self):
       self.assertEqual("The Prancing Pony", self.pub.name) 

   def test_customer_buys_drink(self):
       self.assertAdd(5, self.till)   