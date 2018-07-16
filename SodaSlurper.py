e, f, c = map(int, input().split())

consumed = 0
empty = e + f
while empty >= c:
    consumed += empty // c
    empty = (empty // c) + (empty % c)

print(consumed)
