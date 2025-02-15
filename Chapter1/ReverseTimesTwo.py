orig = int(input()) 
reverse = (orig%10) * 100 + ((orig // 10) % 10) * 10 + orig // 100
print(reverse * 2)