

players = ["Jim", "Peter", "Jack", "Sam"]
rotation = [0, 1, 2, 0]

for i in range(len(players)):
    if rotation[i] == 2:
        for j in range(len(players)):
            print(players[i % len(players)])