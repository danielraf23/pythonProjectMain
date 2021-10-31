class Card:
    def __init__(self,value,suit):
        if type(value) is not int:
            raise TypeError('invalid type')
        elif value<1 or value>14:
            raise ValueError('invalid value')
        else:
            self.value=value
        if suit in ['♥','♠','🔶','♣']:
            self.suit = suit
        else:
            raise ('invalid suit type')
        self.full_card = [suit,value]
        self.value_names = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 'Jack', 12: 'Qween', 13: 'King',14: 'Ace'}

    # a method that checks which card is bigger, depends on value and suit
    def __gt__(self, other):
        rules={"🔶":1,"♣":2,"♥":3,"♠":4}

        if self.value == other.value:
           print("self.suit ==",self.suit)
           if rules[self.suit] > rules[other.suit]:
               return True
           else:
               return False

        elif self.value > other.value:
            return True
        else:
            return False

    # a method that return printable values
    def __repr__(self):
        return f"{self.value_names[self.value]} {self.suit}"


if __name__=="__main__":
    card1=Card(9,"🔶")
    print(card1)



















