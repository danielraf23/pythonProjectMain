from Game_cards.Card import Card
from Game_cards.DeckOfCards import DeckOfCards
from Game_cards.Player import Player
from Game_cards.CardGame import CardGame

player1 = Player('aba',26 )
player2 = Player('Dani',26)


game = CardGame(player1.name,player2.name,26)


print(f"{game.player1}\n{game.player2}")

for i in range(10):
    a = game.player1.get_card()
    b = game.player2.get_card()
    print(f"{game.player1.name}: {a}\t{game.player2.name}: {b}")
    if a.__gt__(b):
        print(f"{game.player1.name} wins the round")
        game.player1.add_card(b)
        game.player2.pack_of_cards.remove(b)
    else:
        print(f"{game.player2.name} wins the round")
        game.player2.add_card(a)
        game.player1.pack_of_cards.remove(a)

if game.get_winner() == game.player1:
    print(F"The winner is: {game.player1.name} with {len(game.player1.pack_of_cards)} cards")
elif game.get_winner() == game.player2:
    print(F"The winner is: {game.player2.name} with {len(game.player2.pack_of_cards)} cards")
elif game.get_winner()== None:
    print("nobody won this time")










