import math
number = int(input())
prime = True
if number == 1:
    prime = False
else:
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            prime = False
            break
if prime:
    print('prime')
else:
    print('not prime')