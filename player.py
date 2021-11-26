from cards import *


class Player:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = Deck(start_empty=True)
        self.current_stake = 0

    def info(self):
        print("-------------------------")
        print("Name: " + str(self.name))
        print("Money: " + str(self.money))
        print("Current Stake: " + str(self.current_stake))
        if len(self.hand.cards) < 1:
            print("No Cards")
        else:
            print("Cards:")
            for card in self.hand.cards:
                print(card.value + " of " + card.suit)
