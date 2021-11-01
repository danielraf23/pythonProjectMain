from Game_cards.DeckOfCards import DeckOfCards
from Game_cards.Player import Player

class CardGame:
    def __init__(self,name1,name2,num_of_cards=26):
        self.deck_of_cards = DeckOfCards()
        if type(name1) is not str:
            raise TypeError ('invalid name type')
        if type(num_of_cards) is not int:
            raise TypeError ('invalid num_of_cards type')
        else:
            self.player1 = Player(name1,num_of_cards)
        if type(name2) is not str:
            raise TypeError ('invalid name type')
        else:
            self.player2 = Player(name2,num_of_cards)
        self.new_game()

    def __repr__(self):
        return f"{self.player1}\n{self.player2}"

    # a method that shuffle and deals cards to the players
    def new_game(self):
        self.deck_of_cards.cards_shuffle()
        self.player1.set_hand(self.deck_of_cards)
        self.player2.set_hand(self.deck_of_cards)

    # a method that returns the player who wins. if draw - None
    def get_winner(self):
        if len(self.player1.pack_of_cards) > len(self.player2.pack_of_cards):
            return self.player1
        elif len(self.player1.pack_of_cards) < len(self.player2.pack_of_cards):
            return self.player2
        else:
            return None


if __name__=="__main__":
    game = CardGame('Gal','Daniel',10)
    print(game)
    print(game.get_winner())
