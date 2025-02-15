orig_string = input()
my_string = orig_string.lower()
output = ""
for letter in my_string:
    if letter in 'aoeiu':
        pass
    else:
        output = output + "." + letter
print(output)

