cost = float(input())
n = int(input())
area = 0

for _ in range(n):
    nums = input().split()
    area += float(nums[0]) * float(nums[1])

print(area * cost)
