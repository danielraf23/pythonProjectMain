from Game_cards.Card import Card
import  random

class DeckOfCards:
    def __init__(self):
        self.Deck_of_cards = []
        suit_list = ['Heart', 'Spade', 'Diamond', 'Club']
        value_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for suit in suit_list:
            for value in value_list:
                card = Card(value, suit)
                self.Deck_of_cards.append(card)

    def shuffle(self):
        random.shuffle(self.Deck_of_cards)


    def deal_one(self):
        return random.choice(self.Deck_of_cards)


if __name__=="__main__":
    deck1 = DeckOfCards()
    print(deck1.Deck_of_cards)
    deck1.shuffle()
    print(deck1.Deck_of_cards)
    print(deck1.deal_one())


