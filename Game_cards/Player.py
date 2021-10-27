from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards
import random

class Player:

    def __init__(self,name, num_of_cards=26):
        self.name=name
        self.num_of_cards=num_of_cards
        if self.num_of_cards>26 or self.num_of_cards<10:
            self.num_of_cards=26
        self.pack_of_cards=[]

    def __repr__(self):
        return f"{self.name}, {self.num_of_cards} {self.pack_of_cards}"

    def set_hand(self, deck_of_cards:DeckOfCards):
        for i in range(self.num_of_cards):
            self.pack_of_cards.append(deck_of_cards.deal_one())


    def get_card(self):
        return random.choice(self.pack_of_cards)

    def add_card(self, card:Card):
        self.pack_of_cards.append(card)


card=Card(9,"Diamond")
deck=DeckOfCards()
player=Player("tov",10)
player.set_hand(deck)
player.get_card()
print(player.add_card(card))
print(player)


