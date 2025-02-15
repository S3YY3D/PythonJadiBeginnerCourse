MaxNumber = 0;
MaxDevisor = 0;
for i in range(20):
    number = int(input())
    if DevisorCounter(number) > MaxDevisor:
        MaxDevisor = DevisorCounter(number)
        MaxNumber = number
prin