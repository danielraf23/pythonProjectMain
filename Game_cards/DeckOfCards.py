import random
from Game_cards.Card import Card

class DeckOfCards:

    def __init__(self):
        self.Deck_of_cards = []
        suit_list = ['♥','♠','🔶','♣']
        value_list = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        for suit in suit_list:
            for value in value_list:
                card=Card(value,suit)
                self.Deck_of_cards.append(card)


    # a method that shuffle the card
    def cards_shuffle(self):
        random.shuffle(self.Deck_of_cards)

    def deal_one(self):
        rand_num = random.choice(self.Deck_of_cards)
        self.Deck_of_cards.remove(rand_num)
        return rand_num


if __name__=="__main__":
    deck1 = DeckOfCards()
    print(deck1.Deck_of_cards)
    deck1.cards_shuffle()
    print(deck1.Deck_of_cards)
    print(deck1.deal_one())


