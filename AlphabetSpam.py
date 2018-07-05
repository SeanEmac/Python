string = input()
length = len(string)

whitespace, lowercase, uppercase, symbol = 0, 0, 0, 0

for i in range(length):
    if string[i] == '_':
        whitespace += 1
    elif string[i].islower():
        lowercase += 1
    elif string[i].isupper():
        uppercase += 1
    else:
        symbol += 1

print(whitespace / length)
print(lowercase / length)
print(uppercase / length)
print(symbol / length)
