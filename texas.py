from tabnanny import check
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
        self.all_in = []  # players who are all in
        self.round_count = 0  # this will decide who the dealer/blinds are
        self.pot = 0
        self.minimum_bet = starting_bet
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

    def check_equal(self):
        for player in self.players:
            if player.current_stake < self.required_stake and player not in self.all_in and player not in self.folded:
                print("\nNot yet equal")
                return False
        print("\nEqual")
        return True

    def player_input(self, player, first, second, third=None):
        s = input("1. {}\n2. {}\n3. {}\n".format(first, second, third)) if third != None else input("1. {}\n2. {}\n".format(first, second))
        if str(s) == "1":
            if first == "Check":
                print("{} Checks\n".format(player.name))
            elif first == "Call":
                print("{} Calls\n".format(player.name))
                self.money_to_pot(player, self.required_stake - player.current_stake)
            elif first == "Call (All-In)":
                print("{} Is All-In ({})".format(player.name, player.money))
                self.all_in.append(player)
                self.money_to_pot(player, player.money)
            else:
                print("Something went wrong with the player_input function")
        elif str(s) == "2":
            if second == "Bet":
                #TODO make it so that players can only bet in intervals of the minimum bet or go all in
                a = input("Amount (min {}): ".format(self.minimum_bet))
                if int(a) >= self.minimum_bet and int(a) <= player.money:
                    print("{} Bets ${}\n".format(player.name, int(a)))
                    self.required_stake += int(a)
                    self.money_to_pot(player, int(a))
                else:
                    print("Invalid amount")
                    self.player_input(player, first, second, third)
            elif second == "Raise":
                a = input("Amount (min {}): ".format(self.required_stake + self.minimum_bet - player.current_stake))
                if int(a) >= self.minimum_bet and int(a) <= player.money:
                    print("{} Raises ${}\n".format(player.name, int(a)))
                    self.required_stake = int(a) + player.current_stake
                    self.money_to_pot(player, int(a))
                else:
                    print("Invalid amount")
                    self.player_input(player, first, second, third)
            elif second == "Fold":
                self.folded.append(player)
            else:
                print("Something went wrong with the player_input function")
        elif str(s) == "3" and third!=None:
            if third == "Fold":
                print("{} Folds".format(player.name))
                self.folded.append(player)
            else:
                print("Something went wrong with the player_input function")
        else:
            print("Invalid input. Please enter one of the numbers provided")
            self.player_input(first, second, third)

    def betting_round(self, first_time=True, preflop=False):
        original_play_rotation = self.players
        if preflop:
            self.players = self.players[-2:] + self.players[:-2]
        for i, player in enumerate(self.players):
            if not first_time:
                if player in self.folded:
                    continue
                else:
                    if player.current_stake < self.required_stake:
                        print(player.name)
                        self.player_input(player, "Call", "Raise", "Fold")
                    elif player.current_stake == self.required_stake:
                        if self.check_equal():
                            print("Everyone is equal")
                            break
                        else:
                            print("An error occured with the check_equal() function")
                            quit()
            else:
                if i == 0:
                    print(player.name)
                    self.player_input(player, "Check", "Bet", "Fold")
                elif i > 0:
                    if self.required_stake > 0 and player.money > self.required_stake:
                        print(player.name)
                        self.player_input(player, "Call", "Raise", "Fold")
                    elif self.required_stake > 0 and player.money <= self.required_stake:
                        print(player.name)
                        self.player_input(player, "Call (All-In)", "Fold")
                    else:
                        print(player.name)
                        self.player_input(player, "Check", "Bet", "Fold")
        self.players = original_play_rotation
        if self.check_equal() == False:
            print("the stake is {}".format(self.required_stake))
            for player in self.players:
                if player in self.folded:
                    print("{} has folded.".format(player.name))
                else:
                    print("{} is in for {}{}".format(player.name, player.current_stake, "All-In" if player in self.all_in else "."))
            print("\n")
            self.betting_round(first_time=False)
        else:
            self.required_stake = 0
            

    def play(self):
        rot = self.round_count % len(self.players)
        self.players = self.players[-rot:] + self.players[:-rot]
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


    def test(self):
        self.betting_round()
        