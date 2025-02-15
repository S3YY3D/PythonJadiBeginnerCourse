highscore = 0
lasthighscore = -1
while True:
    age = int(input())
    if age == -1:
        break
    else:
        if age > highscore:
            lasthighscore = highscore
            highscore = age
        elif age > lasthighscore:
            lasthighscore = age
print(highscore, lasthighscore)