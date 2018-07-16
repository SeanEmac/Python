import sys

for line in sys.stdin.readlines():
    M, P, L, E, R, S, N = map(int, line.split())
    mosquito = M
    pupae = P
    larve = L
    for i in range(N):
        M = pupae // S
        P = larve // R
        L = mosquito * E

        mosquito = M
        pupae = P
        larve = L
    print(M)
