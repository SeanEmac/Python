n = int(input())
possible = False

for _ in range(n):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b == c:
        possible = True
    elif a - b == c:
        possible = True
    elif b - a == c:
        possible = True
    elif a * b == c:
        possible = True
    elif b / a == c:
        possible = True
    elif a / b == c:
        possible = True
    else:
        possible = False

    if possible:
        print("possible")
    else:
        print("impossible")

