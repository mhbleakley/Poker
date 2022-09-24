from cards import *


class Player:

    def __init__(self, name, money, hand=None):
        self.name = name
        self.money = money
        self.hand = [] if hand == None else hand  # all collections of cards will be considered decks
        self.current_stake = 0

    def get_player_info(self):
        return self.name, self.money, self.hand

    def info(self):
        print("-------------------------")
        print("Name: " + str(self.name))
        print("Money: $" + str(self.money))
        print("Current Stake: $" + str(self.current_stake))
        if len(self.hand.cards) < 1:
            print("No Cards")
        else:
            print("Cards:")
            for card in self.hand.cards:
                print(card.value + " of " + card.suit)
