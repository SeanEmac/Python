word = input()
hiss = False

for i in range(len(word)-1):
    if word[i] == 's' and word[i+1] == 's':
        hiss = True

if hiss:
    print("hiss")
else:
    print("no hiss")
