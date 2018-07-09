word = input()
output = ""
output += word[0]

for i in range(len(word)-1):
    if word[i] != word[i+1]:
        output += word[i+1]

print(output)
