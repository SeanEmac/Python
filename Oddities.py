n = int(input())
nums = [int(input()) for x in range(n)]

for i in range(n):
    if nums[i] % 2 == 0:
        print(nums[i], "is even")
    else:
        print(nums[i], "is odd")