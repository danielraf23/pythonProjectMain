from unittest import TestCase
from Game_cards.Card import Card


class TestCard(TestCase):

    def setUp(self):
        print('setUp')
        self.card=Card(9,"🔶")


    def test__init__(self):
        self.assertEqual(self.card.value,9)
        self.assertEqual(self.card.suit,"🔶")

    def test__init__2(self):
        with self.assertRaises(TypeError):
            self.card.value=Card("abc", "abc")
        with self.assertRaises(ValueError):
            self.card.value=Card(15, "🔶")
        with self.assertRaises(ValueError):
            self.card.value=Card(-2, "🔶")


    def test__gt__(self):
        self.card2 = Card(9, "♣")
        self.assertEqual(self.card.value,self.card2.value)
        self.assertNotEqual(self.card.suit,self.card2.suit)
        self.assertGreater(self.card2,self.card)
        self.assertIsNot(self.card, self.card2)

    def test__gt__2(self):
        self.other = Card(9, "♣")
        with self.assertRaises(TypeError):
            self.other.value("abc","abc")
        with self.assertRaises(ValueError):
            self.card.value = Card(15, "🔶")
        with self.assertRaises(ValueError):
            self.card.value = Card(-2, "🔶")





