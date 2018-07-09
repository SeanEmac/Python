from collections import Counter
N = int(input())

for i in range(N):
    G = int(input())
    nums = map(int, input().split())
    count = Counter(nums)
    answer = [k for k, v in count.items() if v < 2]
    print("Case #{}: {}" .format(i+1, answer[0]))
