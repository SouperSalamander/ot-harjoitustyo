import unittest
from src.numberTheory import Operations

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.calc = Operations(12,18)

    def test_gcf(self):
        self.assertEqual(self.calc.gcf(), "Step 1: 18 / 12 = 1 remainder: 6\nStep 2: 12 / 6 = 2 remainder: 0\nThe Greatest Common Factor is 6") 