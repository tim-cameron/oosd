class Card:

    card_value = 0
    card_values = [("Ace", int(1)), ("Two", int(2)), ("Three", int(3)), ("Four", int(4)), ("Five", int(5)),
                   ("Six", int(6)), ("Seven", int(7)), ("Eight", int(8)), ("Nine", int(9)), ("Ten", int(10)),
                   ("Jack", int(10)), ("Queen", int(10)), ("King", int(10))]
    card_suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

    def create_card(self, value, suit):
        self.card_name = str(self.card_values[value][0] + " of " + self.card_suits[suit])

    def get_value(self, value):
        self.card_value = int(self.card_values[value][1])

    def __init__(self, value, suit):
        self.create_card(value, suit)
        self.get_value(value)

    def __str__(self):
        return self.card_name

    
