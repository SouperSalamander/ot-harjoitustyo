import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_initial_correct(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_adds_correctly(self):
        self.maksukortti.lataa_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 30.0)

    def test_decreases_correctly(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_no_change(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_true(self):
        amount = self.maksukortti.ota_rahaa(500)

        self.assertEqual(amount, True)
    
    def test_false(self):
        amount = self.maksukortti.ota_rahaa(1500)

        self.assertEqual(amount, False)
