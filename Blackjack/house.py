
class House:
    cards = []
    total = 0
    def draw_cards(self, amount):
        for c in range(amount):
            self.cards.append(self._deck.deal_card())
    def __init__(self, src_deck):
        self._deck = src_deck
        self.draw_cards(1)
    def win(self):
        print ":( You lost."
        print ""
        print "Press enter to play again!"
        answer = raw_input()

        self.newGame = True
    def lose(self):
        print "You win!"
        print ""
        print "Press enter to play again!"
        answer = raw_input()

        self.newGame = True
    def check_score(self, player_score=21):
        if (self.total == 21):
            self.win()
        elif (self.total > 21):
            self.lose()
        elif (self.total > player_score):
            self.win()
        elif (self.total < 18):
            self.draw_cards(1)
            self.display(player_score)
        else:
            self.lose()

                
    def display(self, player_score = 21):
        self.total = 0
        print ""
        print "\t\t\t- Houses hand -"
        print ""
        for c in self.cards:
            print "\t\t\t" + c.card_name
            self.total = self.total + c.card_value

            if (c.card_value == 1 and self.total < 12):
                self.total += 10
        print ""
        print " \t\t\tTotal of ", self.total

        return self.check_score(player_score)
