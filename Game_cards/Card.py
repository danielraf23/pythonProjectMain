class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
        self.full_card = [suit,value]

    def __repr__(self):
        return f"{self.value} {self.suit}"

    # a method that checks which card is bigger, depends on value and suit
    def __gt__(self, other):
        rules={"Diamond":1,"Spade":2,"Heart":3,"Club":4}

        if self.value == other.value:
           if rules[self.suit] > rules[other.suit]:
               return True
           else:
               return False

        elif self.value > other.value:
            return True
        else:
            return False





if __name__=="__main__":
    Card1 = Card(ace[1],'Diamond')
    Card2 = Card(ace[1],'Spade')

    print(Card1.__gt__(Card2))
