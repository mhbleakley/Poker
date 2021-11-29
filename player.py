from cards import *


class Player:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = Deck(start_empty=True)  # all collections of cards will be considered decks
        self.current_stake = 0  # how much they have put in for the current round of betting (not how much they have in the pot overall)

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
