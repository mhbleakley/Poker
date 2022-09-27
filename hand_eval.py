
import random

class Card:

    def __init__(self, code):
        self.code = code
        self.suit = code[1]
        rank = "23456789TJQKA"
        for i, val in enumerate(rank):
            if code[0] == val:
                self.rank = i


class Deck:

    def __init__(self):
        self.cards = []
        rank = "23456789TJQKA"
        suit = "DSHC"
        for s in suit:
            for r in rank:
                self.cards.append(Card("{}{}".format(r, s)))
        random.shuffle(self.cards)

        
deck = Deck()

five = [deck.cards[:5]]

def eval_five(hand):
    