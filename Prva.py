R, C = map(int, input().split())
word = "reallyreallylongword"

lines = [input() for _ in range(R)]

for line in lines:
    subLine = line.split('#')
    for sub in subLine:
        if len(sub) >= 2:
            if sub < word:
                word = sub

for i in range(C):
    swap = ''.join([lines[j][i] for j in range(R)])
    subLine = swap.split('#')
    for sub in subLine:
        if len(sub) >= 2:
            if sub < word:
                word = sub

print(word)
