

count = 5
players = ["Jim", "Peter", "Jack", "Sam"]
rotation = []

place = count % len(players)

# print(place)

for i, player in enumerate(players[:place]):
    rotation.append(len(players) - place + i)

for i, player in enumerate(players[place:]):
    rotation.append(i)

for item in rotation:
    print(item)
