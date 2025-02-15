#convert 1+1+3+1+3 to 1+1+1+3+3
expression = input()
numbers = expression.split('+')
numbers.sort()
output = '+'.join(numbers)
print(output)