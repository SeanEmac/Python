L, N = map(int, input().split())

occupancy = 0
refused = 0
for i in range(N):
    com = input().split()
    if com[0] == 'enter':
        if (occupancy + int(com[1])) > L:
            refused += 1
        else:
            occupancy += int(com[1])
    else:
        occupancy -= int(com[1])

print(refused)
