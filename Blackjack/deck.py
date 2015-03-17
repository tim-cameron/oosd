import card
import random
CARD_SUITS = 4
CARD_VALUES = 13

class Deck:


    card_array = [];

    def __init__(self, shuffler):
        self.shuffler = shuffler
        self.create_deck()

    def create_deck(self):
        for x in range(0,CARD_SUITS):
            for y in range(0,CARD_VALUES):
                _suit = x
                _value = y
                _card = card.Card(_value, _suit)
                self.card_array.append(_card)
        self.shuffle()


    def shuffle(self):
        self.shuffler.shuffle(self.card_array)


    def deal_card(self):
        _rand = random.randint(0, len(self.card_array) - 1)
        _ret = self.card_array[_rand]
        self.card_array.remove(_ret)
        return _ret
        
    def __str__(self):
        ret = ""
        ret_count = 0
        for i in self.card_array:
            ret += str(i) + "\n"
            ret_count += 1

        return ret + "Count : " + str(ret_count)