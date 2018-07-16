prob = [0,0]

for x in range(2):
    a1, b1, a2, b2 = map(int, input().split())
    nums = []
    for i in range(a1, b1 + 1):
        for j in range(a2, b2 + 1):
            nums.append(i + j)

    prob[x] = (sum(nums) / len(nums))

if prob[0] < prob[1]:
    print("Emma")
elif prob[1] < prob[0]:
    print("Gunnar")
else:
    print("Tie")