import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    # def test_compare_3_1_returns_3_is_greater_than_1(self):
    #     self.assertEqual("3 is greater than 1", compare(3, 1))
    
    def test_compare__greater_than(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare__less_than(self):
        self.assertEqual("4 is less than 11", compare(4, 11))

    def test_compare__equal(self):
        self.assertEqual("both numbers are equal", compare(21, 21))