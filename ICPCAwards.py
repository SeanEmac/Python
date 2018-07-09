N = int(input())
winners = []
uni = []

for _ in range(N):
    entry = input()
    university, team = entry.split()
    if university not in uni:
        uni.append(university)
        winners.append(entry)
    if len(uni) == 12:
        break

for i in range(len(winners)):
        print(winners[i])
