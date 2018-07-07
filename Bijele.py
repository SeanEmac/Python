correct = [1, 1, 2, 2, 2, 8]
nums = input().split()
diff = []
for i in range(6):
    diff.append(correct[i] - int(nums[i]))

for x in diff:
    print(x, end=" ")


