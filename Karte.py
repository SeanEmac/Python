line = input()
cards = [line[i:i+3] for i in range(0, len(line), 3)]
setCards = set(cards)

if len(cards) > len(setCards):
    print("GRESKA")
else:
    numP = 0
    numK = 0
    numH = 0
    numT = 0
    for x in range(len(cards)):
        card = cards[x]
        if card[0] == 'P':
            numP += 1
        elif card[0] == 'K':
            numK += 1
        elif card[0] == 'H':
            numH += 1
        else:
            numT += 1

    print(13 - numP, 13 - numK, 13 - numH, 13 - numT)



