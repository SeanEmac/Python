word = input()
T = 0
G = 0
C = 0
score = 0

for i in range(len(word)):
    if word[i] == 'T':
        T += 1
    elif word[i] == 'G':
        G += 1
    else:
        C += 1

if T > 0 and G > 0 and C > 0:
    score += min(T, G, C) * 7

score += (T ** 2)
score += (G ** 2)
score += (C ** 2)
print(score)
