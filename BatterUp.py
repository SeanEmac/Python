n = int(input())
scores = input().split()

length = 0
total = 0

for x in range(n):
    if scores[x] != '-1':
        length += 1
        total += int(scores[x])

print(total / length)
