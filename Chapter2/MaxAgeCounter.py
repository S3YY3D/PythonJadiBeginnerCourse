highscore = 0
while True:
    age = int(input())
    if age == -1:
        break
    else:
        if age > highscore:
            highscore = age
print(highscore)