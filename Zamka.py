L = int(input())
D = int(input())
X = int(input())
correct = []


def add(x):
    total = 0
    while x > 0:
        total = total + (x % 10)
        x = x // 10
    return total


for i in range(L, D+1):
    if add(i) == X:
        correct.append(i)

print(min(correct))
print(max(correct))