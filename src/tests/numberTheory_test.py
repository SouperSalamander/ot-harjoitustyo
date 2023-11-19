import unittest
from numberTheory import Operations

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.calc = Operations(12,18)

    def test_gcf(self):
        self.assertEqual(self.calc.gcf(), 6)