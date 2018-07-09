e, f, c = map(int, input().split())

consumed = 0
empty = e + f
print(consumed, empty)
while empty >= c:
    consumed += empty // c
    empty = (empty // c) + (empty % c)
    print(consumed, empty)

print(consumed)