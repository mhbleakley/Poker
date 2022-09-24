from email.utils import encode_rfc2231
import os
from cards import *

class CardPrinter:

    def __init__(self, table=False, solid=True):
        if table:
            self.table = []
        self.hand = []
        self.SDCH = ["♠", "♦", "♣", "♥"] if solid else ["♤", "♢", "♧", "♡"]

    def get_symbol(self, card):
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
        for i, suit in enumerate(suits):
            if card.suit == suit:
                return self.SDCH[i]

    def get_value(self, card):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        display_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for i, value in enumerate(values):
            if card.value == value:
                return display_values[i]


    def set_hand(self, cards):
        self.hand = cards

    def set_table(self, cards):
        self.table = cards

    def display(self):
        msg = ""
        card_edge = "+----+"
        card_row = "|    |"
        card_value_long = "|{}  |"
        card_value = "|{}   |"

        def print_cards(cards):
            msg = ""
            for i in range(5):
                row = ""
                for card in cards:
                    if i == 0 or i == 4:
                        row += " " + card_edge
                    if i == 1:
                        val = self.get_value(card)
                        if len(str(val)) > 1:
                            row += " " + card_value_long.format(val)
                        else:
                            row += " " + card_value.format(val)
                    if i == 2:
                        row += " " + card_value.format(self.get_symbol(card))
                    if i == 3:
                        row += " " + card_row
                msg += row + "\n"
            return msg
        
        if self.table:
            msg += print_cards(self.table)
            msg += "\n\n"
        msg += print_cards(self.hand)

        lines = os.get_terminal_size()[1]
        msg_lines = len(msg.split("\n"))

        disp = ""
        for i in range(lines - msg_lines):
            disp += "\n"
        disp += msg        

        print(disp)
        


deck = Deck(start_empty=False, start_shuffled=False)
deck.shuffle()

my_cards = deck.cards[0:2]

cp = CardPrinter(table=True, solid=False)

cp.set_hand(my_cards)
cp.set_table(deck.cards[2:5])



cp.display()