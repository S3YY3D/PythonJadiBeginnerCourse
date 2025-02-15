import random
number = random.randint(1, 99)
while True:
    guess = int(input())
    if guess == number:
        print('doroste!, adad', number, 'javab bood!')
        break
    elif guess < number:
        print('bishtar!')
    else:
        print('kamtar!')
