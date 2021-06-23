import unittest
from src.customer import *
from src.drinks import *
from src.pub import *

class TestCustomer(unittest.TestCase):

       def setUp(self):
        self.customer = Customer("Craig Smith", 100)
        self.drink = Drinks("Beer", 5)

       def test_customer_has_name(self):
        self.assertEqual("Craig Smith", self.customer.name) 
        self.assertEqual(100, self.customer.wallet) 

        
       def test_customer_buys_drink(self):
        self.assertLess(0,self.customer.wallet)

       
         