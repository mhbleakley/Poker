from cards import *
from player import *

# TODO where to hold players who fold?
# TODO betting function capable of checking that stakes match


class Texas:

    def __init__(self, player_list):
        self.deck = Deck()  # standard deck
        self.burn_pile = Deck(start_empty=True)  # all collections of cards will be considered decks
        self.table = Deck(start_empty=True)
        self.players = player_list
        self.out = []  # where to hold players who have folded but are still playing
        self.pot = 0
        self.minimum_bet = 50
        self.rotation = [0 for i in range(len(self.players))]
        self.rotation[0] = 1  # small blind
        self.rotation[1] = 2  # big blind
        self.current_raise = 0

    def info(self):
        print("--------GAME INFO--------")
        print("Players:")
        for player in self.players:
            player.info()
        print("-------------------------")
        print("Pot: $" + str(self.pot))
        print("-------------------------")
        print("To Stay: $" + str(self.current_raise))
        print("-------------------------")
        if len(self.table.cards) < 1:
            print("No Cards On Table")
        else:
            print("Table: ")
            for card in self.table.cards:
                print(card.value + " of " + card.suit)
        print("-------------------------")
        if len(self.burn_pile.cards) < 1:
            print("No Cards In Burn Pile")
        else:
            print("Burn Pile: ")
            for card in self.burn_pile.cards:
                print(card.value + " of " + card.suit)
        print("-------------------------")

    # deals cards from top of deck to a given destination.
    # must be a deck/have a .cards attribute
    def deal_from_top(self, destination):
        # TOP CARD IS LAST CARD IN LIST FOR ALL DECKS
        destination.cards.append(self.deck.cards[-1])
        self.deck.cards.pop()

    # deals cards from top of deck to players until each player has 2 cards
    def deal(self):
        for i in range(2):
            for player in self.players:
                self.deal_from_top(player.hand)

    # handles transactions from players to pot and adjusts their stakes
    def money_to_pot(self, player, amount):
        if not amount > player.money:
            self.pot = self.pot + amount
            player.money = player.money - amount
            player.current_stake = player.current_stake + amount
        else:
            print("Not enough funds")

    # forced initial bet for small and big blinds
    def blinds(self):
        max_raise = 0
        for i, player in zip(self.rotation, self.players):
            self.money_to_pot(player, self.minimum_bet * i)  # transfer blind based on rotation
            if self.minimum_bet * i > max_raise:  # if the blind is bigger than the current required stake
                max_raise = self.minimum_bet * i  # make the new stake the biggest
        self.current_raise = max_raise  # update required stake

    # check for equal stakes
    def stakes_equal(self):
        for player in self.players:
            if player.current_stake < self.current_raise:
                return False
        return True

    def bet(self, blind_round=False):
        if not blind_round:
            for player in self.players:
                # if player needs to call and can
                if player.current_stake < self.current_raise and player.money < self.current_raise - player.current_stake:
                    print(player.name + ", you need " + str(self.current_raise - player.current_stake) + " to stay in.")
                    print("1. Call ($" + str(self.current_raise - player.current_stake) + ")")
                    print("2. Raise")
                    print("3. Fold")
                    ans = input()
                    if str(ans) == "1":
                        self.money_to_pot(player, self.current_raise - player.current_stake)
                        print(player.name + " Calls (" + str(self.current_raise - player.current_stake) + ")")
                    elif str(ans) == "2":
                        r = input("Raise By: $")
                # if player can check
                elif player.current_stake == self.current_raise:
                    print(player.name + ", it is your turn")
                    print("1. Check")
                    print("2. Raise")
                    print("3. Fold")
                    i = input()

    def reveal(self, flop=False):
        self.deal_from_top(self.burn_pile)
        self.deal_from_top(self.table)
        if flop:
            self.deal_from_top(self.table)
            self.deal_from_top(self.table)
        if len(self.table.cards) < 1:
            print("No Cards On Table")
        else:
            print("Table: ")
            for card in self.table.cards:
                print(card.value + " of " + card.suit)

    def play(self):
        self.blinds()
        self.deal()
        self.bet(blind_round=False)
        self.reveal(flop=True)
        self.info()
