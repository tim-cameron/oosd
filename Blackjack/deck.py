import card
import random

class Deck:
    card_array = [];
    
    def __init__(self):
        self.create_deck();

    def create_deck(self):
        for l in range(52):
            _conflict = True
            while(_conflict == True):
                _suit = random.randint(0, 3)
                _value = random.randint(0, 12)
                _card = card.Card(_value, _suit)
                _conflict = False
                for c in self.card_array:
                    if (c.card_name == _card.card_name):
                        _conflict = True
            
            self.card_array.append(_card)
            
    def deal_card(self):
        _rand = random.randint(0, len(self.card_array) - 1)
        _ret = self.card_array[_rand]
        self.card_array.remove(_ret)
        return _ret
        
