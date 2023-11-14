import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.card = Maksukortti(1000)
        self.lessCard = Maksukortti(100)

    def test_money_added_cheap(self):
        self.kassa.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.4)

    def test_money_added_yum(self):
        self.kassa.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1004.0)

    def test_correct_change_cheap(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(340), 100)

    def test_correct_change_yum(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)

    def test_lunch_added_cheap(self):
        self.kassa.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassa.edulliset, 1)

    def test_lunch_added_yum(self):
        self.kassa.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassa.maukkaat, 1)

    def test_money_less_cheap(self):
        self.kassa.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_money_less_yum(self):
        self.kassa.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_returned_change_cheap(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(140), 140)

    def test_returned_change_yum(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(300), 300)

    def test_no_lunch_added_cheap(self):
        self.kassa.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassa.edulliset, 0)

    def test_no_lunch_added_yum(self):
        self.kassa.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassa.maukkaat, 0)

    def test_card_cheap(self):
        cheapCard = self.kassa.syo_edullisesti_kortilla(self.card)

        self.assertEqual(self.card.saldo_euroina(), 7.60)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(cheapCard, True)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_card_yum(self):
        yumCard = self.kassa.syo_maukkaasti_kortilla(self.card)

        self.assertEqual(self.card.saldo_euroina(), 6.0)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(yumCard, True)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_card_less_cheap(self):
        cheapCard = self.kassa.syo_edullisesti_kortilla(self.lessCard)

        self.assertEqual(self.lessCard.saldo_euroina(), 1.0)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(cheapCard, False)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_card_less_yum(self):
        yumCard = self.kassa.syo_maukkaasti_kortilla(self.lessCard)

        self.assertEqual(self.lessCard.saldo_euroina(), 1.0)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(yumCard, False)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_adding_to_card(self):
        self.kassa.lataa_rahaa_kortille(self.card,1000)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1010.0)
        self.assertEqual(self.card.saldo_euroina(), 20.0)

    def test_return(self):
        self.kassa.lataa_rahaa_kortille(self.card,-1)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)
        self.assertEqual(self.card.saldo_euroina(), 10.0)

    def test_str(self):
        self.assertEqual(str(self.card), "Kortilla on rahaa 10.00 euroa")
