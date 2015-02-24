
class Player:
    cards = []
    playing = True
    newGame = False
    turn = True
    total = 0
    def draw_cards(self, amount):
        for c in range(amount):
            self.cards.append(self._deck.deal_card())
    def __init__(self, src_deck):
        self._deck = src_deck
        self.draw_cards(2)
        

    def win(self):
        print "You win!"
        print ""
        print "Press enter to play again!"
        answer = raw_input()

        self.newGame = True


    def lose(self):
        print ":( You lost."
        print ""
        print "Play again? Y/N : "
        print "Press enter to play again!"
        answer = raw_input()

        self.newGame = True
    def check_score(self):
        if (self.total == 21): # check for victory by blackjack first and foremost
            self.playing = False
            self.win()
            return self.turn
        elif (self.total > 21):
            self.playing = False
            self.lose()
            return self.turn
        while(True): # loop until h or s entered
            answer = raw_input("(h)it or (s)tand? : ")

            if (answer.lower() == "h"):
                self.draw_cards(1)
                self.display()
                break
            elif (answer.lower() == "s"):
                self.turn = False
                break

        return self.turn
    
    def display(self):
        self.total = 0 # reset total to 0
        print "- Players hand - "
        print ""
        for c in self.cards:
            print c.card_name
            self.total = self.total + c.card_value

            if (c.card_value == 1 and self.total < 12):
                self.total += 10

        print ""
        print " Total of ", self.total

        return self.check_score()

        
