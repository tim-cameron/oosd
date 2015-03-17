import random
import deck
class ShuffleStrategyA:
    ## OPTION 1
    def __init__(self):
        pass

    def shuffle(self, cards):
        random.shuffle(cards)

class ShuffleStrategyB:
    ## OPTION 2
    def __init__(self):
        pass

    def shuffle(self, cards):
        for i in range(0, len(cards)):
            temp = cards[i]
            rnd = random.randint(0,len(cards) - 1)
            cards[i] = cards[rnd]
            cards[rnd] = temp

class ShuffleStrategyC:
    ## OPTION 3
    def __init__(self):
        pass

    def shuffle(self, cards):
        for i in range(0, len(cards), 2):
            temp = cards[i]
            rnd = random.randrange(1, len(cards), 2)
            cards[i] = cards[rnd]
            cards[rnd] = temp

class ShuffleStrategyD:
    ## OPTION 4
    def __init__(self):
        pass

    def shuffle(self, cards):
        for x in range(52):
            rndA = random.randint(0,len(cards) - 1)
            rndB = random.randint(0,len(cards) - 1)
            temp = cards[rndA]
            cards[rndA] = cards[rndB]
            cards[rndB] = temp
