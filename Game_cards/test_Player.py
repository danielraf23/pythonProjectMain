from unittest import TestCase, mock
from unittest.mock import patch
from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards
from Game_cards.Player import Player



class TestPlayer(TestCase):

    def setUp(self):
        print('Set Up')
        self.player1=Player('daniel',10)
        self.deck=DeckOfCards()

    def tearDown(self):
        print("tearDown")

    # check for valid arguments for player
    def test__init__(self):
        self.assertEqual(self.player1.name,'daniel')
        self.assertEqual(self.player1.num_of_cards,10)

    # check for invalid types of arguments for player
    def test__init__2(self):
        with self.assertRaises(TypeError):
            self.player1=Player(12,23)
        with self.assertRaises(TypeError):
            self.player1=Player('asd','asd')

    def test__init__3(self):
        self.player2=Player('gal',84)
        self.player3=Player('zaki',0)
        self.assertEqual(self.player2.num_of_cards,26)
        self.assertEqual(self.player3.num_of_cards, 26)

    @mock.patch('Game_cards.DeckOfCards.DeckOfCards.deal_one',
                return_value= Card(9,'♣'))
    def test_set_hand(self,mock_card):
        self.player1.num_of_cards=1
        self.deck3=DeckOfCards()
        self.player1.set_hand(self.deck3)
        self.assertIn(mock_card.return_value, self.player1.pack_of_cards)
        self.assertEqual(mock_card.return_value, Card(9, '♣'))
        self.assertNotIn(Card(7, '♣'), self.player1.pack_of_cards)




    def test_get_card(self):
        self.player1.num_of_cards=1
        self.player1.set_hand(self.deck)
        print(self.player1.pack_of_cards)
        self.assertEqual(self.player1.pack_of_cards[0],self.player1.get_card())
        self.assertIn(self.player1.get_card(),self.player1.pack_of_cards)

    def test_add_card(self):
        self.card=Card(4,"🔶")
        self.player1.add_card(self.card)
        self.assertIn(self.card,self.player1.pack_of_cards)
        self.card2 = Card(7, "🔶")
        self.player1.add_card(self.card2)
        self.assertIn(self.card2,self.player1.pack_of_cards)
        self.assertEqual(len(self.player1.pack_of_cards),2)


    def test_add_card2(self):
        with self.assertRaises(ValueError):
            self.card = Card(20, '♣')
            self.player1.add_card(self.card)
            self.assertIn(self.card, self.player1.pack_of_cards)

    def test_add_card3(self):
        self.player1.num_of_cards = 3
        self.card = Card(8, '♣')
        with self.assertRaises(ValueError):
            self.player1.add_card(self.card)
            self.player1.add_card(self.card)
