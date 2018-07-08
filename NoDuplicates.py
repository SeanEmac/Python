words = input().split()
repeat = False

for i in range(len(words)):
    count = 0
    word = words[i]
    for x in range(len(words)):
        if word == words[x]:
            count += 1
            if count > 1:
                repeat = True

if repeat:
    print("no")
else:
    print("yes")
