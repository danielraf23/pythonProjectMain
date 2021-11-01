from unittest import TestCase
from Game_cards.CardGame import CardGame
from Game_cards.Player import Player
from Game_cards.DeckOfCards import DeckOfCards


class TestCardGame(TestCase):

    def setUp(self):
        print("Set Up")
        self.player1 = Player('dani', 15)
        self.player2 = Player('avi', 15)
        self.game=CardGame(self.player1.name, self.player2.name,15)
        self.deck = DeckOfCards()

    def tearDown(self):
        print("tearDown")


    def test__init__(self):
        self.assertEqual(self.player1.name, self.player1.name)
        self.assertEqual(self.player1.num_of_cards, self.player1.num_of_cards)
        self.assertEqual(len(self.deck.Deck_of_cards), 52)
        for i in self.deck.Deck_of_cards:
            self.assertEqual(self.deck.Deck_of_cards.count(i), 1)


    def test__init__2(self):
        with self.assertRaises(TypeError):
            self.player1=Player(23,20)
            self.player2=Player(43,17)
        with self.assertRaises(TypeError):
            self.player2=Player('avi','fgh')
            self.player1=Player('dani','werw')

    def test_new_game(self):
        self.assertEqual(len(self.game.player1.pack_of_cards), self.game.player1.num_of_cards)
        self.assertEqual(len(self.game.player2.pack_of_cards), self.game.player2.num_of_cards)

    def test_get_winner(self):
        self.game.player1.pack_of_cards.pop()
        self.assertGreater(len(self.game.player2.pack_of_cards),len(self.game.player1.pack_of_cards))
        self.assertEqual(self.game.get_winner(),self.game.player2)