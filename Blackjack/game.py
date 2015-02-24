import player
import house
import deck


class Game:
    def run_game(self):

        _p = self.player.display()
        
        if (self.player.turn == False):
            self.house.display(self.player.total)

        self.new_game()


    def new_game(self): # couldn't get it to start a new game :/
        def setup():
            self.deck = deck.Deck()
            self.player = player.Player(self.deck)
            self.house = house.House(self.deck)
            

        def play():
            self.run_game()

        def new():
            self.new_game()
            
        setup()
        play()
        new()
