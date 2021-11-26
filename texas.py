from cards import *
from player import *


class Texas:

    def __init__(self, player_list):
        self.deck = Deck()  # standard deck
        self.burn_pile = Deck(start_empty=True)
        self.table = Deck(start_empty=True)
        self.players = player_list
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

    def money_to_pot(self, player, amount):
        if not amount > player.money:
            self.pot = self.pot + amount
            player.money = player.money - amount
        else:
            print("Not enough funds")

    def blinds(self):
        for i, player in zip(self.rotation, self.players):
            if i == 1:
                self.money_to_pot(player, self.minimum_bet)
            if i == 2:
                self.money_to_pot(player, self.minimum_bet * 2)
                self.current_raise = self.minimum_bet * 2

    def bet(self, blind_round=False):
        pass
        # if this is a blind round, start at the player directly after the big blind
        # else start betting at the small blind
        # given that it is not a blind round, the first player can check, raise, or fold
        # if he raises the players after him must match his stake or raise it to stay in
