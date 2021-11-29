import random


class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if self.suit == "Diamonds" or "Hearts":  # color is implied by the suit of the card
            self.color = "Red"
        elif self.suit == "Clubs" or "Spades":
            self.color = "Black"
        else:
            print("Error: Invalid Suit")


class Deck:

    def __init__(self, start_empty=False, start_shuffled=True):
        self.cards = []
        if not start_empty:
            self.generate()
            if start_shuffled:
                self.shuffle()

    def generate(self):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def shuffle(self, amount=3):
        for i in range(amount):
            random.shuffle(self.cards)


# deck test
# deck = Deck(start_empty=False, start_shuffled=False)
# for card in deck.cards:
#     print(str(card.value) + " of " + str(card.suit))
# deck.shuffle()
# print()
# for card in deck.cards:
#     print(str(card.value) + " of " + str(card.suit))
