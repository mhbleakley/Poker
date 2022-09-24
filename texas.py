from cards import *
from player import *
from button_tracker import *
import sys

class Texas:

    def __init__(self, player_list, starting_bet):
        self.valid_game = True  # true when there are at least two players who can both place the minimum bet
        self.deck = Deck()  # standard deck
        self.burn_pile = Deck(start_empty=True)
        self.community_cards = Deck(start_empty=True)
        self.players = player_list  # small blind starts at i = 0
        self.folded = []  # where to hold players who have folded but are still playing
        self.round_count = 0  # this will decide who the dealer/blinds are
        self.pot = 0
        self.minimum_bet = starting_bet
        self.stage = "PREFLOP"
        self.required_stake = 0
        self.bt = ButtonTracker(self.players)


    # check before the game begins that there are in fact at least
    # two players who both have enough money to start
    def initial_check(self):
        if len(self.players) < 2:
            self.valid_game = False
        for player in self.players:
            if player.money < self.minimum_bet:
                self.valid_game = False

    def deal_from_top(self, destination):
        # TOP CARD IS LAST CARD IN LIST FOR ALL DECKS
        destination.append(self.deck.cards[-1])
        self.deck.cards.pop()

    # deals cards from top of deck to players until each player has 2 cards
    def deal(self):
        for i in range(2):  # each player gets 2 cards
            for player in self.players:
                self.deal_from_top(player.hand)  # each card comes from the top

    # handles transactions from players to pot and adjusts their stakes
    def money_to_pot(self, player, amount):
        if not amount > player.money:
            self.pot = self.pot + amount
            player.money = player.money - amount
            player.current_stake = player.current_stake + amount
        else:
            print("Not enough funds")

    # forced initial bet for small and big blinds
    def collect_blinds(self):
        self.money_to_pot(self.bt.small(), self.minimum_bet)  # small blind
        self.money_to_pot(self.bt.big(), 2 * self.minimum_bet) # big blind
        self.required_stake = 2 * self.minimum_bet

    def burn_and_turn(self, flop=False):
        self.deal_from_top(self.burn_pile)
        self.deal_from_top(self.community_cards)
        if flop:
            self.deal_from_top(self.community_cards)
            self.deal_from_top(self.community_cards)

    def pre_flop_action(self):
        pass

    def action(self):
        pass

    def play(self):
        print("Doing inital check")
        self.initial_check()
        if not self.valid_game:
            sys.exit("Not enough players or not all players have enough money.")
        print("The button is " + self.bt.smalln())
        print("Collecting blinds")
        self.collect_blinds()
        print("Blinds collected\n")
        for p in self.players:
            print(p.name, str(p.money))
        print("\nDealing Cards\n")
        self.deal()
        for p in self.players:
            print("{}'s hand:".format(p.name))
            for c in p.hand:
                print(c.get_card_info())
            print("\n")
        