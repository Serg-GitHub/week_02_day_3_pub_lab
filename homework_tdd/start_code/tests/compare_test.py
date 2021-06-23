import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_4_4_returns_numbers_are_the_same(self):
     self.assertEqual("numbers are the same", compare(4, 4))

