names = input().split('-')
initials = ""

for x in range(len(names)):
    initials += names[x][0]

print(initials)
