from texas import *

john = Player("John", 10000)
jim = Player("Jim", 10000)

players = [john, jim]

texas = Texas(players)
texas.deal()
texas.blinds()
texas.bet(blind_round=True)
texas.info()
