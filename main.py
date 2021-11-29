from texas import *

john = Player("John", 10000)
sam = Player("Sam", 10000)
aaron = Player("Aaron", 10000)

players = [john, sam, aaron]

texas = Texas(players)
texas.play()
