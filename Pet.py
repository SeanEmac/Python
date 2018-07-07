winner = 0
total = 0
for i in range(5):
    scores = input().split()
    nums = [int(x) for x in scores]
    if sum(nums) > total:
        total = sum(nums)
        winner = i+1

print(winner, total)
