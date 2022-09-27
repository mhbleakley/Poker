from email.utils import encode_rfc2231
from operator import add
import os
from cards import *
import platform

class CardPrinter:

    def __init__(self, table=False, solid=True):
        if table:
            self.table = []
        self.hand = []
        # if platform.system() == "Windows":
        #     self.SDCH = ["S", "D", "C", "H"]
        # else:
        self.SDCH = ["♠", "♦", "♣", "♥"] if solid else ["♤", "♢", "♧", "♡"]

    # resolves suit of card for symbol (symbols found in SDCH)
    def get_symbol(self, card):
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
        for i, suit in enumerate(suits):
            if card.suit == suit:
                return self.SDCH[i]

    # resolves value for code
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

    # displays cards/additional information to the terminal
    # will display player options if any argument is given for it
    # additional information will print to the right of the terminal
    def display(self, player_options=None, additional_info=None):
        term = os.get_terminal_size()

        msg = "" # populate this to be printed to terminal screen

        # making the pieces of cards
        card_edge = "+----+"
        card_row = "|    |"
        card_value_long = "|{}  |" # one less space so that you can represnt longer values (i.e. 10) and not have spacing issues
        card_value = "|{}   |"

        def print_cards(cards): # function to print cards specifically
            msg = ""
            for i in range(5):
                row = ""
                for j, card in enumerate(cards):
                    val = self.get_value(card)
                    suit = self.get_symbol(card)
                    if j > 0: # add a space between cards
                        row += " "
                    if i == 0 or i == 4: # print top/bottom of card
                        row += card_edge
                    if i == 1: # card value
                        row += card_value_long.format(val) if len(str(val)) > 1 else card_value.format(val)
                    if i == 2: # card suit
                        row += card_value.format(suit)
                    if i == 3: # generic row
                        row += card_row
                msg += row + "\n"
            return msg
        
        if self.table:
            msg += "Table:\n"
            msg += print_cards(self.table)
            msg += "\n\n"
        
        msg += "Your Hand:\n"
        msg += print_cards(self.hand)
        
        if player_options != None:
            msg += "\n\nOptions:\n"
            for i, option in enumerate(player_options):
                msg += "{}. {}\n".format(i + 1, option)

        term_lines = term[1]
        msg_lines = msg.split("\n")

        # ATTEMPT TO ADD INFROMATION TO SIDE OF SCREEN
        # final_msg = ""
        # if additional_info:
        #     add_lines = additional_info.split("\n")
        #     longest_msg_line = 0
        #     for line in msg_lines:
        #         if len(line) > longest_msg_line:
        #             longest_msg_line = len(line)
        #     for i, line in enumerate(msg_lines):
        #         if i < len(add_lines):
        #             final_msg += line.ljust(longest_msg_line - len(line)) + "\t|\t" + add_lines[i] + "\n"
        #         else:
        #             final_msg += line + "\n"

        disp = ""
        for i in range(term_lines - len(msg_lines)):
            disp += "\n"
        disp += msg
        # disp += final_msg        

        print(disp)
        


deck = Deck(start_empty=False, start_shuffled=False)
deck.shuffle()

my_cards = deck.cards[0:2]

cp = CardPrinter(table=True, solid=True)

cp.set_hand(my_cards)
cp.set_table(deck.cards[2:7])

options = ["Check", "Raise", "Fold"]

cp.display(player_options=options)
