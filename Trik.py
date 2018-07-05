movesList = input()

a = 1
b = 0
c = 0

for i in range(len(movesList)):
    move = movesList[i]

    if move == 'A':
        temp = b
        b = a
        a = temp
    if move == 'B':
        temp = c
        c = b
        b = temp
    if move == 'C':
        temp = a
        a = c
        c = temp

if a == 1:
    print(1)

if b == 1:
    print(2)

if c == 1:
    print(3)
