from player import Player
from texas import Texas

john = Player("John", 10)
sam = Player("Sam", 10)
aaron = Player("Aaron", 10)
paul = Player("Paul", 10)
gus = Player("Gus", 10)

players = [john, sam, aaron, paul, gus]

texas = Texas(players, 1)
texas.test()