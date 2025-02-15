#read 10 names and make them Pascal Case
names = []
for i in range(10):
    name = input()
    standard_name = name[0].upper() + name[1:].lower()
    names.append(standard_name)
for name in names:
    print(name)