highscore = 0
wins = 0
for i in range(30):
    score = int(input())
    if score == 3:
        wins += 1
    highscore += score
print(highscore, wins)