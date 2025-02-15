import math
def DevisorCounter(number):
    devisor = 1
    for i in range(1, number//2+1):
        if number % i == 0:
            devisor += 1
    return devisor;


MaxNumber = 0;
MaxDevisor = 0;
for i in range(20):
    number = int(input())
    if DevisorCounter(number) > MaxDevisor:
        MaxDevisor = DevisorCounter(number)
        MaxNumber = number
print(MaxNumber, MaxDevisor)