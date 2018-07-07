n = int(input())
nums = [int(input()) for x in range(n)]
total = 0

for i in range(n):
    total += ((nums[i]//10) ** (nums[i] % 10))

print(total)
